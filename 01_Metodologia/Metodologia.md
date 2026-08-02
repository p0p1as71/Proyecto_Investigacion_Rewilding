---
tipo: capitulo
estado: cerrado
version: 1.0
fecha: 2026-08-02
depende_de: ["00_Gobernanza/Criterios_de_Evidencia.md", "00_Gobernanza/Glosario.md", "00_Gobernanza/Decisiones_Editoriales.md", "00_Gobernanza/Convenciones_de_Redaccion.md"]
---

# Metodología

## 1. Objeto

Este informe analiza la implementación del rewilding en España a través de tres ejes
—vacíos legales para especies semidomesticadas, desplazamiento de actividad
agroganadera en zonas de despoblación, y cuestionamientos académicos sobre
efectividad ecológica— más un análisis transversal del uso del concepto jurídico y
científico de "reintroducción" (`05_Reintroducciones/`), una síntesis del modelo
Rewilding Spain / Rewilding Europe (`07_Rewilding_Spain/`) y una matriz de
contrastación de afirmaciones (`10_Matriz_de_Evidencia/`).

El objeto no es evaluar si el rewilding "funciona" en sentido general, sino si
afirmaciones concretas —jurídicas, ecológicas, terminológicas— resisten el
contraste con fuente primaria. Ver Glosario para las acepciones exactas de
"reintroducción", "rewilding pasivo", "proxy ecológico" y demás términos operativos.

## 2. Preguntas de investigación

| Eje | Pregunta |
|---|---|
| Jurídico | ¿Qué régimen legal se aplica de facto a cada especie/proxy utilizado, y coincide con el que se invoca públicamente? |
| Social | ¿Qué evidencia sostiene, en cada sentido, la tesis de desplazamiento de actividad agroganadera? |
| Científico | ¿Qué grado de consenso académico existe sobre los mecanismos ecológicos invocados (control top-down, reducción de incendios, restauración de procesos)? |
| Terminológico | ¿El uso público de "reintroducción" cumple los requisitos de la UICN y del art. 55 Ley 42/2007, o son usos divergentes? |
| Institucional | ¿Qué afirma cada actor (Rewilding Spain, Rewilding Europe, administraciones, crítica académica, crítica agraria) y con qué nivel de fuente se sostiene? |

Cada pregunta se traduce en afirmaciones concretas (AF-###) en
`10_Matriz_de_Evidencia/Matriz.md`, cada una con su bloque R1-R4
(Criterios de Evidencia §12).

## 3. Identificación y recogida de fuentes

- **N0 (primaria propia):** textos normativos descargados y archivados con hash
  SHA-256 en `12_Referencias/`; entrevistas propias en `09_Entrevistas/`;
  documentación obtenida por transparencia.
- **N1-N3 (normativa indirecta, académica, dictámenes):** búsqueda en fuente oficial
  o repositorio del editor (BOE, EUR-Lex, DOI del artículo). Se prioriza el PDF del
  artículo o dictamen sobre el resumen o la nota de prensa que lo comenta.
- **N4-N6 (institucional, prensa, parte no institucional):** se recoge tal cual se
  publica, con `consultado:` obligatorio (Criterios §13). No se corrige ni mejora la
  redacción de la fuente al parafrasear.
- **N7:** no se "recoge" — es la interpretación que este informe construye sobre
  las anteriores, y se marca `[INFERENCIA]` cuando conecta hechos de fuentes
  distintas (Criterios §3).

Toda fuente nueva pasa primero por clasificación N0-N7 antes de citarse en cualquier
capítulo. La clasificación no es responsabilidad del capítulo que la usa — se fija
una vez en `12_Referencias/` y se hereda.

## 4. Tratamiento de conflictos

Cuando dos fuentes del mismo nivel discrepan (ej. Nores et al. 2024 vs. Bartolomé
et al. 2026, ambas N2), este informe no arbitra. Se describen ambas posiciones según
Criterios de Evidencia §4. La resolución de un conflicto solo se admite ante consenso
posterior documentado, nunca por preferencia editorial.

## 5. Principio de simetría aplicado

Toda afirmación se somete al mismo estándar probatorio independientemente de quién la
emita — Rewilding Spain, Rewilding Europe, administración, crítica académica o
crítica agraria (Criterios §11). En la práctica esto significa que este informe
buscará activamente evidencia en contra de sus propias hipótesis de partida, no solo
a favor. Cuando esa búsqueda no encuentre nada en ningún sentido, se aplica DE-006:
"no se ha localizado evidencia", nunca "no existe evidencia".

## 6. Unidad de análisis: la afirmación (AF-###)

La unidad mínima de este informe no es el capítulo ni el párrafo, sino la afirmación
individual, indexada como AF-### en la Matriz de Evidencia. Cada AF-### lleva:
nivel de fuente, bloque R1-R4, y si aplica, marcador (`[NO LOCALIZADO]`,
`[INFERENCIA]`, `[CONFLICTO N#]`, `[ATRIBUCIÓN NO DISTINGUIBLE]`). Los capítulos
narrativos (02-08) son la exposición en prosa de conjuntos de AF-### relacionadas;
la Matriz es su versión tabular y trazable.

## 7. Fuera de alcance

- Litigios judicializados sobre fincas concretas entre Rewilding Spain y terceros:
  no se han documentado (ver `04_Marco_Social/`, eje 2) y no se investigan de forma
  especulativa.
- Evaluación de impacto económico agregado del turismo de naturaleza asociado: fuera
  de alcance salvo que aparezca en fuente N0-N3 directamente relevante para una
  pregunta de investigación ya formulada.
- Comparación con proyectos de rewilding fuera de España: se cita solo cuando una
  fuente N2 la usa como término de comparación metodológico (ej. bibliografía sobre
  livestock rewilding europeo en general).

Las limitaciones de *acceso* (qué no hemos podido consultar, qué sigue embargado o en
desarrollo) se tratan en `01_Metodologia/Limitaciones.md`, no aquí — esta sección
fija el alcance pretendido, no las restricciones encontradas al perseguirlo.

## 8. Relación con otros capítulos

```
Metodologia (este documento)
  -> Limitaciones          (restricciones de acceso encontradas)
  -> Marco_Juridico          -> resuelve entradas [PENDIENTE] del Glosario (§14 Criterios)
  -> Marco_Cientifico
  -> Marco_Social
  -> Reintroducciones        (depende de Marco_Juridico + Marco_Cientifico)
  -> Especies                (depende de Reintroducciones)
  -> Rewilding_Spain_vs_Europe
  -> Evidencia_Empirica + Gobernanza_Cientifica
  -> Matriz_de_Evidencia      (agrega AF-### de todos los anteriores)
  -> Informe_Critico          (síntesis final)
```

---
*Bloqueos abiertos: ninguno propio. Condiciona el inicio de todos los capítulos 02-08
según sus respectivas `depende_de`.*
