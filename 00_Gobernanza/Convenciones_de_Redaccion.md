---
tipo: gobernanza
estado: cerrado
version: 0.1
fecha: 2026-08-02
depende_de: ["00_Gobernanza/Criterios_de_Evidencia.md", "00_Gobernanza/Glosario.md"]
---

# Convenciones de Redacción

Estilo, no metodología. Cumplimiento obligatorio para que un capítulo pase a
`verificado` (Criterios de Evidencia §10, condición 11).

---

## 1. Nomenclatura científica

- Nombres científicos siempre en cursiva: *Bison bonasus*, *Equus ferus przewalskii*,
  *Bos primigenius*.
- Primera mención en cada capítulo: nombre común + científico entre paréntesis —
  "bisonte europeo (*Bison bonasus*)". Menciones posteriores: nombre común.
- Género abreviado solo tras primera mención completa: *B. bonasus*.
- Autoridad taxonómica: no se incluye salvo que la fuente citada la use y sea
  relevante para el argumento.
- Tauros: no es un taxón. Se escribe en redonda, minúscula, y en primera mención se
  precisa su naturaleza (programa de cría selectiva, no especie).

## 2. Legislación

- Primera mención en cada capítulo, cita completa: "Ley 42/2007, de 13 de diciembre,
  del Patrimonio Natural y de la Biodiversidad". Posteriores: "Ley 42/2007".
- Artículos: "art. 55.1 Ley 42/2007". Nunca "el artículo cincuenta y cinco" ni "la ley
  dice que".
- Normativa UE: "Reglamento (UE) 2016/429" — paréntesis en "(UE)" obligatorio.
- Directivas: "Directiva 92/43/CEE (Hábitats)" en primera mención.
- Reales decretos: "RD 630/2013" tras primera mención completa.
- Versión consolidada: se indica cuando la afirmación depende de un artículo
  modificado (Criterios §13).

## 3. Fechas

- Formato ISO en metadatos, tablas, cabeceras YAML y campos `consultado:` /
  `archivado:`: `2026-08-02`.
- En prosa se admite formato largo: "2 de agosto de 2026". Nunca formatos ambiguos
  tipo 02/08/2026.
- Datación paleontológica: "cal BP" con el rango tal como lo da la fuente, sin
  redondear.

## 4. Citas textuales y paráfrasis

- Cita textual: entre comillas angulares «…» en español, comillas rectas "…" en
  inglés, con localizador (artículo, página, sección). Máximo 15 palabras, una por
  fuente y documento (Criterios §6).
- Paráfrasis: sin comillas, con atribución explícita — "Nores et al. sostienen que…".
  Nunca se parafrasea tan cerca del original que resulte indistinguible de una cita.
- Cita dentro de cita: se evita. Si la fuente A cita a B, se busca B directamente; si
  no se localiza, se marca "citado en A" y `[NO LOCALIZADO]` para el original.
- Elipsis dentro de cita: […]. Nunca se omite texto que altere el sentido.
- Traducciones: si se traduce una cita, se indica "(trad. propia)". El original queda
  en `12_Referencias/`.

## 5. Nomenclatura institucional

- "Rewilding Spain" y "Rewilding Europe" siempre completos, nunca "Rewilding" a secas
  (DE-004).
- Denominación legal en primera mención: "Fundación Española de Renaturalización
  (Rewilding Spain)".
- Cargos: nombre + cargo + organización en primera mención. Posteriores: apellido.
- Siglas: desarrolladas en primera mención de cada capítulo — REGA, MITECO, UICN,
  LPI, EEI. No se asume que el lector llegue desde el capítulo anterior.

## 6. Marcadores

Se escriben en mayúsculas, entre corchetes, sin negrita:

`[NO LOCALIZADO]` · `[INFERENCIA]` · `[CONFLICTO N#]` ·
`[ATRIBUCIÓN NO DISTINGUIBLE]` · `[PENDIENTE]` · `[TODO]`

`[TODO]` es el único marcador que impide `verificado` por sí mismo. Los demás son
estados legítimos y permanentes de una afirmación.

## 7. Tablas

- Toda tabla lleva encabezado de fila y, si compara fuentes, columna de nivel N0-N7.
- Toda tabla lleva una línea de fuentes inmediatamente debajo, en cursiva.
- Celda sin dato: `[NO LOCALIZADO]`, nunca vacía ni con guion.
- Tablas comparativas entre especies: mismo orden de filas en todo el repositorio —
  bisonte europeo, caballo de Przewalski, tauros, buitre negro, otros.
- Máximo 6 columnas. Por encima, se parte en dos tablas.

## 8. Figuras

- Numeración por capítulo: Fig. 02-1, Fig. 02-2.
- Pie obligatorio: qué muestra, fuente, fecha, y si es elaboración propia.
- Cartografía: sistema de referencia y fecha de los datos en el pie.
- Fotografía propia: se marca N0 y se referencia el archivo original.
- Ninguna figura reproduce material de terceros sin verificar su licencia; en su
  defecto se enlaza, no se incorpora.

## 9. Prosa

- Voz activa. Sujeto explícito en toda afirmación atribuible: quién afirma qué.
- Prohibido el sujeto difuso: "se considera", "hay quien sostiene", "muchos expertos".
  Si no puede nombrarse la fuente, la frase no entra.
- Prohibidos los adjetivos valorativos sobre actores: "polémico", "controvertido",
  "cuestionable" aplicados a personas u organizaciones. Sí se admiten sobre
  afirmaciones concretas cuando estén justificados ("discutible desde el art. 55").
- Condicional de rumor prohibido: "habría liberado", "sería el responsable".
- Longitud: párrafos de un solo argumento. Un párrafo, una idea contrastable.

## 10. Estructura de archivo

Todo archivo .md del repositorio:
1. Cabecera YAML: `tipo`, `estado`, `version`, `fecha`, `depende_de`.
2. Título H1 igual al concepto del archivo.
3. Registro de cambios entre versiones, si las hay.
4. Cuerpo.
5. Pie con notas de estado y bloqueos abiertos.

Nombres de archivo: sin tildes, sin espacios, guion bajo como separador,
`Mayuscula_Inicial_Por_Palabra.md`.

---
*Documento de estilo. Cambios aquí no invalidan capítulos cerrados, pero obligan a
una pasada de armonización registrada en `11_Cronologia/`.*
