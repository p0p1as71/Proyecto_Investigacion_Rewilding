---
tipo: mapa
estado: en_redaccion
version: 0.1
fecha: 2026-08-02
depende_de: []
---

# Mapa del Repositorio

> Diagrama Mermaid — se renderiza automáticamente en la vista de lectura de
> Obsidian. No es contenido citable; es navegación visual.

```mermaid
flowchart TD
    G["00 · Gobernanza<br/>Criterios · Decisiones · Glosario · Convenciones"]
    M["01 · Metodología<br/>+ Limitaciones"]

    G --> M

    M --> J["02 · Marco Jurídico"]
    M --> C["03 · Marco Científico"]
    M --> S["04 · Marco Social"]

    J --> R["05 · Reintroducciones"]
    C --> R

    R --> E1["06 · Bisonte Europeo"]
    R --> E2["06 · Buitre Negro"]
    R --> E3["06 · Caballo Przewalski"]
    R --> E4["06 · Caballo Serrano"]
    R --> E5["06 · Tauros"]

    E1 --> RS["07 · Rewilding Spain vs. Europe"]
    E2 --> RS
    E3 --> RS
    E4 --> RS
    E5 --> RS

    C --> EV["08 · Evidencia Empírica"]
    J --> GC["08 · Gobernanza Científica"]
    C --> GC

    RS --> MTX["10 · Matriz de Evidencia<br/>65 AF-###"]
    EV --> MTX
    GC --> MTX
    S --> MTX

    MTX --> CR["11 · Cronología"]
    MTX --> RF["12 · Referencias<br/>N0-N7"]

    MTX --> CO["13 · Conclusiones"]
    CR --> CO
    RF --> CO

    CO --> RC["14 · Recomendaciones"]

    RC --> IC["Informe_Critico.md<br/>síntesis final"]

    EN["09 · Entrevistas<br/>(sin bloquear nada)"] -.-> J
    EN -.-> C
    EN -.-> S

    AN["99 · Anexos<br/>(buzón temporal)"] -.-> G

    style G fill:#2d2d2d,color:#fff
    style MTX fill:#7a1f1f,color:#fff
    style CO fill:#1f4d7a,color:#fff
    style RC fill:#1f4d7a,color:#fff
    style IC fill:#3a6b35,color:#fff
    style EN stroke-dasharray: 5 5
    style AN stroke-dasharray: 5 5
```

## Lectura del diagrama

- **Flechas sólidas** = dependencia real (`depende_de` en la cabecera YAML).
- **Flechas punteadas** = relación informativa, no bloqueante (Entrevistas y
  Anexos no figuran en el `depende_de` de ningún capítulo, Criterios §10).
- **Nodo rojo** (Matriz) = punto de convergencia obligado — todo hallazgo pasa
  por ahí antes de llegar a Conclusiones.
- **Nodos azules** (Conclusiones, Recomendaciones) = los dos capítulos nuevos,
  con la regla dura de separación entre "qué muestra la evidencia" y "qué se
  propone hacer al respecto".

---
*Actualizar este diagrama cada vez que se añada o reordene un capítulo — mismo
riesgo de desincronización ya detectado antes en `README.md` e
`Informe_Critico.md`.*
