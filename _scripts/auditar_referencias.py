#!/usr/bin/env python3
"""
Auditoría de consistencia entre:
  - menciones de AF-### en los capítulos narrativos (02-08)
  - filas AF-### realmente registradas en 10_Matriz_de_Evidencia/Matriz.md
  - IDs de referencia (N0-001, N1-002...) registrados en 12_Referencias/Referencias.md
  - uso real de esos IDs de referencia en el cuerpo de los capítulos

No genera contenido nuevo — solo diagnostica huecos y desincronización, para
decidir qué automatizar primero. Uso:

    python3 _scripts/auditar_referencias.py

Próximo paso natural (no implementado todavía): si se adopta de forma
consistente la cita `[N#-ID]` en el cuerpo de cada capítulo (Criterios §6, hoy
sin uso real — ver diagnóstico), este mismo script podría generar automáticamente
las tablas de 10_Matriz_de_Evidencia/Matriz.md y 12_Referencias/Referencias.md en
lugar de solo auditarlas.
"""

import re
import glob
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

CHAPTER_GLOBS = [
    "02_Marco_Juridico/*.md", "03_Marco_Cientifico/*.md", "04_Marco_Social/*.md",
    "05_Reintroducciones/*.md", "06_Especies/*.md", "07_Rewilding_Spain/*.md",
    "08_Evidencia/*.md",
]

AF_PATTERN = re.compile(r"\bAF-(\d{3})\b")
REFID_PATTERN = re.compile(r"\bN[0-7]-(\d{3})\b")
INLINE_CITE_PATTERN = re.compile(r"\[N[0-7]-\d{3}\]")  # formato Criterios §6


def chapter_files():
    files = []
    for pattern in CHAPTER_GLOBS:
        files.extend(sorted((ROOT).glob(pattern)))
    return [f for f in files if f.is_file()]


def matriz_af_ids():
    path = ROOT / "10_Matriz_de_Evidencia" / "Matriz.md"
    text = path.read_text(encoding="utf-8")
    return set(AF_PATTERN.findall(text))


def referencias_ids():
    path = ROOT / "12_Referencias" / "Referencias.md"
    text = path.read_text(encoding="utf-8")
    return set(m.group(0) for m in re.finditer(r"\bN[0-7]-\d{3}\b", text))


def main():
    files = chapter_files()

    mentioned_af = {}
    for f in files:
        text = f.read_text(encoding="utf-8")
        for num in AF_PATTERN.findall(text):
            mentioned_af.setdefault(num, []).append(str(f.relative_to(ROOT)))

    registered_af = matriz_af_ids()
    mentioned_set = set(mentioned_af.keys())

    print("=" * 70)
    print("1. Consistencia AF-### (capítulos <-> Matriz)")
    print("=" * 70)
    missing_from_matriz = mentioned_set - registered_af
    if missing_from_matriz:
        print(f"[AVISO] {len(missing_from_matriz)} AF-### mencionadas en capítulos "
              f"pero SIN fila en Matriz.md:")
        for n in sorted(missing_from_matriz):
            print(f"  AF-{n} <- {', '.join(mentioned_af[n])}")
    else:
        print("Ninguna AF-### huérfana. Toda mención en capítulos tiene fila en Matriz.")

    only_in_matriz = registered_af - mentioned_set
    print(f"\nAF-### en Matriz.md sin mención textual explícita en ningún capítulo: "
          f"{len(only_in_matriz)}")
    print("(Esperable: la Matriz numera afirmaciones aunque el capítulo no repita "
          "el ID literal 'AF-###' en su prosa — no es necesariamente un error.)")

    print()
    print("=" * 70)
    print("2. Uso real de la cita formal [N#-ID] (Criterios de Evidencia §6)")
    print("=" * 70)
    total_inline_cites = 0
    for f in files:
        text = f.read_text(encoding="utf-8")
        hits = INLINE_CITE_PATTERN.findall(text)
        total_inline_cites += len(hits)

    if total_inline_cites == 0:
        print("[DIAGNÓSTICO] 0 citas en formato [N#-ID] encontradas en ningún capítulo.")
        print("La regla de Criterios §6 existe pero no se ha aplicado todavía en la")
        print("prosa real — las citas actuales son narrativas ('verificado contra BOE,")
        print("consultado 2026-08-02 [N1]'), no el tag [N1-001] enlazable.")
        print()
        print("Consecuencia para la automatización: no se puede generar Referencias.md")
        print("ni Matriz.md automáticamente todavía, porque no hay un ID citable de forma")
        print("consistente en el texto de origen. Primer paso real de automatización:")
        print("retrofit — pasar los capítulos ya 'en_redaccion' e insertar el tag [N#-ID]")
        print("junto a cada afirmación verificada, no escribir el script antes de eso.")
    else:
        print(f"{total_inline_cites} citas en formato [N#-ID] encontradas.")

    print()
    print("=" * 70)
    print("3. IDs registrados en Referencias.md")
    print("=" * 70)
    refs = referencias_ids()
    print(f"{len(refs)} IDs de referencia registrados: {', '.join(sorted(refs))}")


if __name__ == "__main__":
    sys.exit(main())
