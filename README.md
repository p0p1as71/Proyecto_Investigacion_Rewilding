# Proyecto Investigación Rewilding — Repositorio

*Última actualización: 2026-08-02.*

Repositorio Obsidian/Git. `Informe_Critico.md` es una vista de síntesis, no el
contenedor del conocimiento — y también es donde vive el estado actualizado de cada
capítulo. El conocimiento vive en los capítulos numerados.

## Reglas de oro

1. Un capítulo no debería redactarse hasta que sus `depende_de` estén `cerrado`
   (Criterios §10). En la práctica, se ha avanzado en paralelo con dependencias en
   `en_redaccion`/`en_revision` cuando era razonable — cada caso queda anotado en
   `11_Cronologia/`, serie B. No es la vía por defecto, es la excepción registrada.
2. **Principio de simetría** (Criterios §11): las afirmaciones institucionales y las
   críticas se evalúan con el mismo estándar. Prevalece sobre cualquier otro criterio.
3. Un artículo que habla del BOE no es el BOE (N0 vs. N1).
4. Alta fiabilidad != alto valor probatorio.
5. **Ausencia de evidencia != evidencia de ausencia** (DE-006): "no se ha localizado"
   nunca se convierte en "no existe" salvo demostración positiva.
6. Un archivo puede tener secciones verificadas de forma independiente sin que el
   archivo entero pase a `verificado` (Criterios §15) — ver anotaciones `> [OK]` dentro
   de cada capítulo.

## Flujo editorial

```
pendiente -> en_redaccion -> en_revision -> verificado -> cerrado
```

`verificado` exige: citas comprobadas una a una (bloque R1-R4, Criterios §12),
enlaces resueltos, legislación contrastada contra N0/N1, terminología conforme al
Glosario, convenciones de redacción aplicadas, y cero marcadores `[TODO]`.

## Estructura (contenido real a fecha de hoy)

```
00_Gobernanza/          Criterios (v0.4) · Decisiones_Editoriales (v0.2, DE-001…006)
                        · Glosario (v0.2) · Convenciones_de_Redaccion — los 4 CERRADOS
01_Metodologia/         Metodologia.md (CERRADO) + Limitaciones.md (en_redaccion)
02_Marco_Juridico/      Marco_Juridico.md — 3 bloqueos abiertos
03_Marco_Cientifico/    Marco_Cientifico.md — 3 bloqueos abiertos
04_Marco_Social/        Marco_Social.md — mayor deuda de verificación N6 del proyecto
05_Reintroducciones/    Reintroducciones.md — tabla comparativa de 5 casos
06_Especies/            5 archivos: Bisonte_Europeo, Buitre_Negro, Caballo_Przewalski,
                        Caballo_Serrano, Tauros
07_Rewilding_Spain/     Rewilding_Spain_vs_Europe.md
08_Evidencia/           Evidencia_Empirica.md + Gobernanza_Cientifica.md
09_Entrevistas/         _index.md (candidatos + solicitudes en curso) +
                        _Plantilla_Entrevista.md — sin entrevistas realizadas aún
10_Matriz_de_Evidencia/ Matriz.md — 65 AF-### registradas
11_Cronologia/          Cronologia.md — serie A (objeto, 27 hitos) + serie B (editorial)
12_Referencias/         Referencias.md (índice N0-N7) +
                        originales/ (1 documento N0 archivado con hash)
13_Conclusiones/        Conclusiones.md — bloqueado hasta que 13 capítulos cierren
14_Recomendaciones/     Recomendaciones.md — depende de Conclusiones
99_Anexos/              vacío
Mapa_Repositorio.md     diagrama Mermaid navegable (Obsidian lo renderiza nativo)
_scripts/               auditar_referencias.py — diagnóstico, no generación aún
```

## Marcadores en uso

`[NO LOCALIZADO]` · `[INFERENCIA]` · `[CONFLICTO N#]` ·
`[ATRIBUCIÓN NO DISTINGUIBLE]` · `[PENDIENTE]` · `[TODO]` · `> [OK]` (sección
verificada de forma independiente, Criterios §15)

## Decisiones transversales resueltas

Ver `Informe_Critico.md` § "Las tres decisiones transversales" para el detalle de:
cierre parcial por sección, prioridad de verificación N6, y el estado real de
`09_Entrevistas/`.

## Estado y próximo paso

El estado capítulo por capítulo vive en `Informe_Critico.md` — se actualiza en cada
sesión y es la referencia, no este README. A fecha de hoy: 12 de 13 capítulos con
contenido redactado (`09_Entrevistas/` sin entrevistas realizadas, pero no
bloqueado); ~20 afirmaciones de la Matriz pendientes de verificación directa;
2 solicitudes de entrevista en curso sin respuesta.
