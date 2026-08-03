---
tipo: sintesis
estado: pendiente
version: 0
fecha: 2026-08-03
depende_de:
  - todos los capítulos en estado cerrado
---
---
tipo: sintesis
estado: pendiente
version: 0.0
fecha: 2026-08-03
depende_de: ["todos los capítulos en estado cerrado"]
---

# Informe Crítico: Desafíos del Rewilding en España

> Síntesis que enlaza los capítulos del repositorio. El desarrollo argumental, con
> fuentes clasificadas N0-N7, vive en las carpetas. Ningún párrafo se escribe hasta
> que el capítulo del que depende está `cerrado`.

## Estado del repositorio (actualizado 2026-08-02)

Flujo: `pendiente -> en_redaccion -> en_revision -> verificado -> cerrado`

| # | Documento | Estado |
|---|---|---|
| 00 | Criterios de Evidencia (v0.4) | **cerrado** — añadida §15 (cierre parcial por sección) |
| 00 | Decisiones Editoriales (v0.2, DE-001…006) | **cerrado** |
| 00 | Glosario (v0.2, estructura) | **cerrado** · 5 entradas `[PENDIENTE]` restantes |
| 00 | Convenciones de Redacción (v0.1) | **cerrado** |
| 01 | Metodología | **cerrado** (YAML corregido para reflejarlo) |
| 01 | Limitaciones | **cerrado** (confirmado por Popi) |
| 02 | Marco Jurídico | en_redaccion · 3 bloqueos abiertos |
| 03 | Marco Científico | en_redaccion · 3 bloqueos abiertos |
| 04 | Marco Social | en_redaccion · 6 de 9 afirmaciones verificadas; 3 bloqueos restantes (cabreros, Manzano-publicación exacta, Resco de Dios) |
| 05 | Reintroducciones | en_redaccion · tabla comparativa 5 especies |
| 06 | Especies (5 archivos) | en_redaccion · regla de cierre parcial por sección ya disponible (§15) |
| 07 | Rewilding Spain vs. Europe | en_redaccion |
| 08 | Evidencia Empírica | en_redaccion |
| 08 | Gobernanza Científica | en_redaccion |
| 09 | Entrevistas | en_redaccion · Prof. Ojanguren acepta entrevista, pendiente fijar fecha/medio |
| 10 | Matriz de Evidencia | en_redaccion · 65 AF-### registradas |
| 11 | Cronología | en_redaccion · series A+B completas |
| 12 | Referencias | en_redaccion · N6 con primeras verificaciones (Oteros-Rozas, Manzano/Azcárate/Hevia) |
| 13 | Conclusiones | pendiente · bloqueada por diseño hasta que 13 capítulos estén cerrado |
| 14 | Recomendaciones | pendiente · depende de Conclusiones |

## Las tres decisiones transversales — resueltas 2026-08-02

1. **Cierre parcial por sección** -> Criterios de Evidencia §15. Regla: el `estado`
   YAML sigue siendo único por archivo; las secciones ya listas se marcan con
   anotación inline (`> [OK] Sección verificada...`); sus AF-### pueden entrar en la
   Matriz con estado V aunque el archivo no esté `cerrado`. Aplicación retroactiva a
   `06_Especies/` pendiente para la próxima pasada de mantenimiento.
2. **Prioridad N6** -> atacada parcialmente: Oteros-Rozas verificada (coincide con
   informe de origen); Manzano/Azcárate/Hevia verificados en identidad y posición
   general (no la publicación exacta "UPA Anuario 2024"). Pendientes: ASAJA Ávila,
   PASTRES (ficha 5/6), cabreros Mallata.com, UGAM-COAG/AIGAS, Resco de Dios,
   Saavedra, Schapira (cadena trófica).
3. **`09_Entrevistas/`** -> aclarado: no bloquea nada (ningún capítulo lo tiene en
   `depende_de`), es contenido N0 potencial no realizado, no una tarea atrasada.
   Añadida plantilla y lista de candidatos a entrevistar surgidos de vacíos ya
   identificados en otros capítulos.

## Añadidos 2026-08-02 (segunda pasada de revisión de Popi)

- **13_Conclusiones/** y **14_Recomendaciones/** creados como capítulos separados
  (no fusionados) — una conclusión describe lo que muestra la evidencia, una
  recomendación prescribe una acción. Ambos bloqueados por diseño hasta que los
  13 capítulos de los que dependen (Conclusiones) estén `cerrado`, no solo
  `en_redaccion`.
- **`Mapa_Repositorio.md`** — diagrama Mermaid navegable en Obsidian, con
  flechas sólidas (dependencia real) y punteadas (relación informativa no
  bloqueante, ej. Entrevistas/Anexos).
- **`_scripts/auditar_referencias.py`** — script de auditoría (no de generación
  todavía). Diagnóstico real al ejecutarlo hoy: **0 citas en formato `[N#-ID]`**
  existen en el cuerpo de ningún capítulo, pese a que Criterios §6 lo exige. La
  automatización completa de Matriz/Referencias requiere primero retrofitear ese
  tag en la prosa ya escrita — no tiene sentido automatizar antes de eso.

## Próximo paso sugerido

Completar la verificación N6 restante de `Marco_Social.md` (7 afirmaciones), o
aplicar retroactivamente las anotaciones de cierre parcial (§15) a los 5 archivos de
`06_Especies/` para que la Matriz refleje su estado real sección por sección.