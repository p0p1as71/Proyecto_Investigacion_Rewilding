---
tipo: entrevista
estado: en_redaccion
version: 0.1
fecha: AAAA-MM-DD
entrevistado: "Nombre completo, cargo, organización"
rol_en_el_proyecto: "ej. director técnico, Junta CLM / crítico académico / ganadero afectado"
modalidad: "presencial / telefónica / videollamada / escrita (email, cuestionario)"
consentimiento_publicacion: "sí / no / parcial — especificar qué partes"
consentimiento_grabacion: "sí / no"
nivel_asignado: "N0 (si hay grabación/transcripción archivada) o N6 (declaración recogida sin archivo verificable)"
depende_de: []
---

# Entrevista: [Nombre del entrevistado]

## 1. Contexto

- **Por qué se entrevista a esta persona:** qué vacío o afirmación pendiente de la
  Matriz (`10_Matriz_de_Evidencia/Matriz.md`) motiva la entrevista. Referenciar
  AF-### concretas si existen.
- **Fecha, duración, modalidad.**
- **Quién realiza la entrevista** (Popi / colaborador).

## 2. Guion previo (opcional, para trazabilidad)

Lista de preguntas preparadas, organizadas por eje del proyecto — facilita que las
respuestas se puedan clasificar directamente contra un capítulo existente:

- Eje jurídico (`02_Marco_Juridico/`): ...
- Eje científico (`03_Marco_Cientifico/`): ...
- Eje social (`04_Marco_Social/`): ...
- Eje terminológico (`05_Reintroducciones/`): ...
- Otro: ...

## 3. Archivo original

- **Ruta:** `12_Referencias/originales/[nombre_archivo]` (audio, transcripción o
  correo).
- **Hash SHA-256** (obligatorio para elevar a N0, Criterios §13): `...`
- **Archivado:** AAAA-MM-DD

Si no hay archivo verificable (ej. conversación telefónica no grabada), la entrevista
se queda en N6, no en N0 — se anota expresamente por qué no se pudo archivar.

## 4. Afirmaciones relevantes (bloque R1-R4, Criterios §12)

Repetir este bloque por cada afirmación extraída que vaya a citarse en algún
capítulo. No mezclar cita textual y paráfrasis en la misma línea (Criterios §3).

```
AF-###
  R1 fuente ......... [Nombre entrevistado], entrevista propia, AAAA-MM-DD [N0/N6]
  R2 archivo ........ 12_Referencias/originales/... · sha256:... (si aplica)
  R3 dice ........... "cita textual <=15 palabras" (Convenciones §4) / paráfrasis fiel
  R4 interpretación . [lectura de este informe] o "lectura literal, sin interpretación"
  Capítulo destino .. ej. 02_Marco_Juridico/Marco_Juridico.md §5
```

## 5. Notas de simetría (Criterios §11)

Si el entrevistado representa una posición de parte (institucional, agraria,
académica crítica), señalar aquí explícitamente que sus afirmaciones se tratan con
el mismo estándar probatorio que cualquier otra fuente del mismo nivel — no se
elevan ni se descartan por el rol de quien habla.

## 6. Pendientes tras la entrevista

- `[TODO]` afirmaciones aún sin trasladar a la Matriz.
- `[PENDIENTE]` puntos que la propia entrevista dejó abiertos y requieren
  contraste adicional.

---
*Plantilla — copiar como nuevo archivo `NombreApellido.md` dentro de
`09_Entrevistas/` y rellenar. No editar este archivo directamente para una
entrevista real.*
