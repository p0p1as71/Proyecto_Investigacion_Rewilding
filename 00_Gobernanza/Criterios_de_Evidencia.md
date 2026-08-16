---
tipo: gobernanza
estado: cerrado
version: 0.5
fecha: 2026-08-16
depende_de: []
---

# Criterios de Evidencia

Documento raíz del proyecto. Fija clasificación, citación y tratamiento de fuentes.
Ninguna afirmación entra en un capítulo sin nivel de fuente asignado.

**Cambios v0.1 -> v0.2:** añadido nivel N0; separadas fiabilidad y valor probatorio;
añadido §4 (conflictos entre fuentes); añadido §11 (principio de simetría);
sustituido el estado binario por flujo editorial de cinco fases (§10).

**Cambios v0.2 -> v0.3:** añadida §12 (regla de reproducibilidad); añadida §13 (regla
de actualización, con fecha de consulta y fecha de archivado obligatorias); añadida
§14 (resolución de la dependencia circular con el Glosario); remitido el estilo a
`00_Gobernanza/Convenciones_de_Redaccion.md` (§8).

**Cambios v0.4 -> v0.5:** §15 (cierre parcial por sección) actualizada — nota de
"aplicación retroactiva pendiente" sustituida por "aplicación retroactiva
completada 2026-08-16", tras aplicar formalmente las anotaciones `> [OK]` a los 5
archivos de `06_Especies/`. Cambio de constatación, no de regla — no requiere
revisión de coherencia en otros capítulos `cerrado` (ninguno de los cerrados usa
§15).

---

## 1. Niveles de fuente

Dos ejes independientes. **Fiabilidad** = cuánto confiamos en que el documento dice
lo que dice. **Valor probatorio** = qué puede demostrar ese documento *para una
afirmación sustantiva* (eficacia ecológica, causalidad, estatus jurídico real).

| Nivel | Tipo | Fiabilidad | Valor probatorio | Notas |
|---|---|---|---|---|
| N0 | Evidencia primaria propia | Máxima | Máximo dentro de su objeto | BOE descargado y archivado con hash, resolución administrativa original, sentencia íntegra, expediente, entrevistas propias, fotografía propia, documentación obtenida por transparencia |
| N1 | Normativa citada indirectamente | Alta | Alto | Texto legal consultado pero no archivado como N0; reglamentos UE, directrices UICN |
| N2 | Académica revisada por pares | Alta | Alto, sujeto a réplica dentro del propio nivel | Ambio, Current Biology, Conservation Science and Practice, Frontiers |
| N3 | Dictamen técnico-administrativo | Alta | Alto en su ámbito; no equivale a norma | Comité Científico MITECO, informes oficiales no normativos |
| N4 | Declaración institucional | **Máxima** para "¿qué dijo X?" | **Bajo** para eficacia o causalidad | Notas de prensa, blogs y comunicados de Rewilding Spain / Rewilding Europe |
| N5 | Prensa | Media | Bajo; válida para fechas y cifras declaradas, no para causalidad | El País, Cadena SER, El Salto, Mongabay |
| N6 | Fuente de parte no institucional | **Máxima** para "¿qué sostiene X?" | **Bajo** para hechos | ASAJA, PASTRES, cabreros, ganaderos, entrevistas de terceros |
| N7 | Interpretación del autor | N/A | **Nulo** — no es evidencia | Análisis que cruza N0-N6 |

Regla dura sobre N0 vs. N1: **un artículo que habla del BOE no es el BOE.** Cuando una
afirmación jurídica dependa de un texto normativo, se archiva el original en
`12_Referencias/` y se eleva a N0. Mientras no esté archivado, se cita como N1.

Regla dura sobre N4 y N6: alta fiabilidad no es valor probatorio. Una declaración
de Rewilding Spain prueba qué declara Rewilding Spain — nada más. Una declaración
de ASAJA prueba qué sostiene ASAJA — nada más. La sintaxis debe reflejarlo
("Rewilding Spain declara que…", no "se ha demostrado que…").

## 2. Rewilding Spain vs. Rewilding Europe

Personas jurídicas distintas. Regla dura:
- Toda cita se atribuye a la organización exacta que la emite, aunque operen como
  socios en el mismo paisaje.
- Si la fuente no permite distinguirlo: `[ATRIBUCIÓN NO DISTINGUIBLE]`.

## 3. Umbral hecho / inferencia

**Hecho** si: consta en texto normativo (N0/N1); es dato verificable no interpretado
(fecha, cifra declarada, cita atribuida); o es conclusión publicada explícitamente
por la fuente citada, no derivada por el autor.

**Inferencia** si: conecta dos hechos mediante razonamiento del autor (causalidad,
patrón), o atribuye motivación no declarada por el actor ("ignoraron", "desoyeron",
"en realidad buscaban").

Regla dura: toda inferencia se etiqueta `[INFERENCIA]` y se justifica en nota al pie
con los hechos de base. Nunca comparte sintaxis con un hecho.

## 4. Conflictos entre fuentes

Regla dura: **cuando existan discrepancias entre fuentes del mismo nivel (N2 vs. N2),
el informe describirá ambas posiciones y no resolverá el conflicto, salvo que exista
un consenso posterior documentado.**

Aplicación:
- El conflicto se marca `[CONFLICTO N#]` y se documenta con ambas posiciones, sus
  argumentos centrales y sus fechas.
- "Consenso posterior documentado" significa: revisión sistemática, dictamen
  técnico-administrativo posterior (N3), cambio normativo (N0/N1) o retractación
  formal. **No cuenta:** mayor número de firmantes, mayor factor de impacto, ni que
  una posición encaje mejor con la tesis del informe.
- Conflicto entre niveles distintos: prevalece el nivel superior **solo dentro de su
  objeto**. Un dictamen N3 sobre estatus legal no zanja un debate N2 sobre
  paleobiogeografía, y viceversa.
- Caso testigo: Nores et al. (2024) vs. Bartolomé, Cassinello, Ceacero et al. (2026)
  y contrarréplica de Nores et al. — se describen las tres piezas; el informe no
  dictamina cuál tiene razón.

## 5. Uso de "no localizado"

`[NO LOCALIZADO]` cuando se ha buscado la fuente primaria y no aparece, o cuando una
fuente secundaria cita un dato sin enlazar el original.

Prohibido rellenar el hueco con suposición razonable. `[NO LOCALIZADO]` es respuesta
válida y final hasta que aparezca fuente.

## 6. Citación

- Cita textual máxima: 15 palabras por fuente; una cita textual por fuente y
  documento. Lo demás se parafrasea.
- Cada cita lleva: autor/organización, fuente, fecha, nivel N0-N7.
- Referencia interna: `[N#-ID]`, con ID en `12_Referencias/`.

## 7. Legislación

- Cita por artículo y apartado exacto ("art. 55.1 Ley 42/2007"), nunca "la ley dice
  que…".
- Se distingue expresamente entre lo que la norma exige y lo que la práctica
  administrativa aplica (ej. REGA frente a Reglamento UE 2016/429).

## 8. Terminología y estilo

Todos los capítulos usan las definiciones fijadas en `00_Gobernanza/Glosario.md`.
Ningún capítulo introduce una acepción alternativa sin registrarla allí primero.

Las convenciones formales (cursivas, formato de fechas, citación de legislación,
tablas, figuras) se fijan en `00_Gobernanza/Convenciones_de_Redaccion.md` y son de
cumplimiento obligatorio para pasar a `verificado`.

## 9. Decisiones editoriales

Toda decisión de estilo, encuadre o terminología con efecto transversal se registra
en `00_Gobernanza/Decisiones_Editoriales.md` con ID, motivo y fecha.

## 10. Flujo editorial

```
pendiente -> en_redaccion -> en_revision -> verificado -> cerrado
```

| Estado | Significa |
|---|---|
| `pendiente` | No iniciado. Dependencias posiblemente sin cerrar |
| `en_redaccion` | Texto en construcción. Puede contener marcadores `[TODO]` |
| `en_revision` | Texto completo, pendiente de revisión de Popi |
| `verificado` | Citas comprobadas una a una, enlaces resueltos, legislación contrastada contra fuente N0/N1, cero marcadores pendientes |
| `cerrado` | Verificado + revisado por Popi. Solo se reabre con entrada en Cronología |

Condiciones para pasar a `verificado` (todas, sin excepción):
1. Toda afirmación tiene nivel N0-N7 asignado.
2. Toda inferencia etiquetada y justificada.
3. Todo hueco marcado `[NO LOCALIZADO]`, no omitido en silencio.
4. Todo conflicto marcado `[CONFLICTO N#]` y descrito sin resolver.
5. Rewilding Spain y Rewilding Europe diferenciados en cada cita que las involucre.
6. Cero marcadores `[TODO]`.
7. Enlaces comprobados y accesibles en la fecha de verificación.
8. Terminología conforme al Glosario; entradas `[PENDIENTE]` usadas por el capítulo, resueltas (§14).
9. Toda afirmación responde R1-R4 (§12).
10. Toda referencia lleva `consultado:` y, si es N0, `archivado:` + hash (§13).
11. Convenciones de redacción aplicadas (`Convenciones_de_Redaccion.md`).

Un capítulo no sale de `pendiente` si algún elemento de su `depende_de` no está
`cerrado`.

## 11. Principio de simetría

**Toda afirmación realizada por Rewilding Spain o Rewilding Europe se evalúa con los
mismos criterios que cualquier crítica formulada contra ellas — y a la inversa.**

Consecuencias operativas:
- "Reduce incendios" (N4) y "no reduce incendios" (N2/N6) requieren ambas evidencia
  del nivel adecuado. Ninguna se acepta por defecto.
- Una afirmación crítica sin respaldo se marca `[NO LOCALIZADO]` exactamente igual que
  una institucional sin respaldo.
- Una fuente de parte crítica (N6) no gana valor probatorio por coincidir con la tesis
  del informe.
- La carga de la prueba no depende de quién habla, sino de qué se afirma.

Este principio prevalece sobre cualquier otro criterio en caso de tensión.

## 12. Regla de reproducibilidad

Toda afirmación debe poder responder a las cuatro preguntas siguientes. Si falta
cualquiera de las cuatro respuestas, la afirmación **no pasa de `en_revision`**.

| # | Pregunta | Se responde con |
|---|---|---|
| R1 | ¿Cuál es la fuente? | Autor/organización, título, fecha de publicación, nivel N0-N7 |
| R2 | ¿Dónde está archivada? | Ruta local en `12_Referencias/` + hash SHA-256 si es N0; URL si es N1-N6 |
| R3 | ¿Qué afirma exactamente? | Cita textual (máx. 15 palabras) o paráfrasis fiel, con localizador (artículo, página, sección) |
| R4 | ¿Cómo se ha interpretado? | Lectura del autor, explícita y separada de R3. Si R3 = R4, se indica "lectura literal, sin interpretación" |

R3 y R4 nunca se funden en la misma frase. La separación entre lo que la fuente dice
y lo que el informe deduce es la aplicación operativa de §3.

Formato mínimo por afirmación, en nota o en el índice de afirmaciones:

```
AF-###
  R1 fuente ......... [N#] Autor, Título, AAAA-MM-DD
  R2 archivo ........ 12_Referencias/xxxx.pdf · sha256:… · consultado 2026-08-02
  R3 dice ........... "…" (art. 55.1) / paráfrasis
  R4 interpretación . […] o "lectura literal"
```

## 13. Regla de actualización

Las fuentes cambian: páginas web se editan, notas de prensa se retiran, la
legislación consolidada se modifica. Dos campos obligatorios en toda referencia:

- **Fecha de consulta** (`consultado: AAAA-MM-DD`) — cuándo se leyó.
- **Fecha de archivado** (`archivado: AAAA-MM-DD`) — cuándo se guardó copia local.

Reglas duras:
- Ninguna fuente N1-N6 se cita sin `consultado`.
- Ninguna fuente asciende a N0 sin `archivado` + hash SHA-256 de la copia.
- Para legislación consolidada se registra además la **versión consolidada** utilizada
  (fecha de la última modificación incorporada al texto consultado). Citar "Ley
  42/2007" sin versión consolidada es insuficiente cuando la afirmación depende de un
  artículo modificado con posterioridad.
- Discrepancia entre la copia archivada y la fuente viva en una consulta posterior:
  no se sobrescribe. Se conserva ambas versiones y se registra el cambio en
  `11_Cronologia/`.

## 14. Dependencia del Glosario (resolución de circularidad)

El Glosario contiene entradas marcadas `[PENDIENTE]` que solo pueden resolverse al
contrastar fuentes N0 durante la redacción del Marco Jurídico. Si el Glosario debiera
estar íntegramente `cerrado` antes de iniciar cualquier capítulo, el proyecto quedaría
bloqueado.

Resolución: el estado del Glosario opera **por entrada**, no solo por documento.
- El Glosario pasa a `cerrado` cuando su **estructura y reglas generales** están
  fijadas, aunque contenga entradas `[PENDIENTE]`.
- Una entrada `[PENDIENTE]` bloquea únicamente los capítulos que usan ese término,
  y solo para pasar a `verificado` — no impide redactarlos.
- Al verificar un capítulo, toda entrada `[PENDIENTE]` que use debe haberse resuelto
  contra fuente N0/N1 en ese mismo acto.

Esta excepción es específica del Glosario. No se extiende a ningún otro documento.

## 15. Cierre parcial por sección

Decisión pendiente desde `06_Especies/Bisonte_Europeo.md`, resuelta ahora.

**Regla:** el estado en la cabecera YAML de un archivo (§10) es único y se refiere
al archivo completo — no se fragmenta el campo `estado`. Lo que sí puede variar por
sección es una **anotación inline** de verificación, usando el siguiente formato al
final de cada apartado (`##`) que esté listo:

```
> [OK] Sección verificada 2026-08-02 — cumple condiciones §10 de forma independiente.
```

**Consecuencias:**
- El archivo permanece en `en_redaccion` (o el estado que le corresponda) mientras
  tenga al menos una sección sin esa anotación.
- Una sección anotada como verificada **no puede reabrirse implícitamente** por
  cambios en otras secciones del mismo archivo — si un cambio posterior la afecta,
  se retira la anotación y se registra el motivo en `11_Cronologia/`, serie B.
- Las afirmaciones (AF-###) de una sección anotada pueden incorporarse a
  `10_Matriz_de_Evidencia/Matriz.md` con estado V aunque el archivo en su conjunto
  no esté `cerrado` — la Matriz opera a nivel de afirmación, no de archivo
  (consistente con cómo ya se ha venido construyendo).
- Esta anotación es informativa, no sustituye las 8 condiciones de `verificado`
  (§10) ni el flujo completo hacia `cerrado`, que sigue siendo responsabilidad de
  Popi sobre el archivo entero.

**Aplicación retroactiva — completada 2026-08-16:** los capítulos de
`06_Especies/` ya contenían, en sus notas de cierre, la identificación de qué
secciones cumplían las condiciones de forma independiente. Esas notas se han
convertido en anotaciones inline formales (`> [OK]`) en la pasada de
mantenimiento del 2026-08-16 — 13 secciones anotadas en los 5 archivos. Al
aplicar la anotación se detectó que algunos pies de página reclamaban cierre de
secciones que en realidad contenían `[PENDIENTE]` sin resolver; esos casos no
recibieron la anotación sin antes verificar directamente el `[PENDIENTE]`
señalado — ver `11_Cronologia/` serie B para el detalle caso por caso.

---
*Documento raíz. Cambios aquí obligan a revisar la coherencia de todos los capítulos
en estado `verificado` o `cerrado`, y a registrar la revisión en `11_Cronologia/`.*
