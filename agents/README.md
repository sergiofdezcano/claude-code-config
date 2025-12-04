# Agentes Especializados

Esta carpeta contiene 9 agentes especializados que se activan automáticamente o bajo demanda para tareas específicas.

## Tabla de Contenidos

- [Visión General](#visión-general)
- [Agentes Disponibles](#agentes-disponibles)
- [Cómo Funcionan](#cómo-funcionan)
- [Instalación](#instalación)
- [Personalización](#personalización)

## Visión General

Los agentes son expertos especializados en dominios específicos. Claude Code los invoca automáticamente cuando detecta tareas relevantes, o puedes invocarlos manualmente cuando necesites su experiencia.

### Características Clave

- **Activación Proactiva**: Algunos agentes se activan automáticamente
- **Herramientas Específicas**: Cada agente tiene acceso a tools relevantes
- **Modelos Optimizados**: Asignación inteligente de modelos (Opus, Sonnet, Haiku)
- **Especialización Profunda**: Expertise en su dominio específico

## Agentes Disponibles

### 1. 🔍 code-reviewer

**Modelo**: Sonnet | **Activación**: Proactiva

Especialista en revisión de código para calidad, seguridad y mantenibilidad.

**Cuándo se usa:**
- Automáticamente después de escribir o modificar código
- Para análisis de seguridad y vulnerabilidades
- Revisión de pull requests

**Checklist de revisión:**
- ✅ Código simple y legible
- ✅ Nombres descriptivos de funciones y variables
- ✅ Sin código duplicado
- ✅ Manejo de errores apropiado
- ✅ Sin secretos expuestos o API keys
- ✅ Validación de entrada implementada
- ✅ Buena cobertura de tests
- ✅ Consideraciones de rendimiento

**Salida:**
- Issues críticos (debe arreglarse)
- Warnings (debería arreglarse)
- Sugerencias (considerar mejorar)
- Ejemplos específicos de cómo arreglar problemas

**Herramientas:** Read, Write, Edit, Bash, Grep

---

### 2. 📚 api-documenter

**Modelo**: Haiku | **Activación**: Proactiva

Crea especificaciones OpenAPI/Swagger, genera SDKs y escribe documentación para desarrolladores.

**Cuándo se usa:**
- Documentación de APIs o generación de librerías cliente
- Crear specs OpenAPI completas
- Generar colecciones Postman/Insomnia

**Áreas de enfoque:**
- Escritura de OpenAPI 3.0/Swagger
- Generación de SDKs y librerías cliente
- Documentación interactiva
- Estrategias de versionado y guías de migración
- Ejemplos de código en múltiples lenguajes
- Documentación de autenticación y errores

**Salida:**
- Especificación OpenAPI completa
- Ejemplos de request/response con todos los campos
- Guía de configuración de autenticación
- Referencia de códigos de error con soluciones
- Ejemplos de uso de SDK
- Colección Postman para testing

**Herramientas:** Read, Write, Edit, Bash

---

### 3. 🐍 python-pro

**Modelo**: Sonnet | **Activación**: Proactiva

Escribe código Python idiomático con features avanzadas como decorators, generators y async/await.

**Cuándo se usa:**
- Refactorización Python
- Optimización de rendimiento
- Features complejas de Python

**Áreas de enfoque:**
- Features avanzadas de Python (decorators, metaclasses, descriptors)
- Async/await y programación concurrente
- Optimización de rendimiento y profiling
- Patrones de diseño y principios SOLID
- Testing comprehensivo (pytest, mocking, fixtures)
- Type hints y análisis estático (mypy, ruff)

**Salida:**
- Código Python limpio con type hints
- Unit tests con pytest y fixtures
- Benchmarks de rendimiento para rutas críticas
- Documentación con docstrings y ejemplos
- Sugerencias de refactorización
- Resultados de profiling de memoria y CPU

**Herramientas:** Read, Write, Edit, Bash

---

### 4. 🗄️ database-architect

**Modelo**: Opus | **Activación**: Bajo demanda

Especialista en arquitectura y diseño de bases de datos, modelado de datos y patrones de escalabilidad.

**Cuándo se usa:**
- Decisiones de diseño de bases de datos
- Modelado de datos complejo
- Planeación de escalabilidad
- Patrones de datos para microservicios
- Selección de tecnología de base de datos

**Expertise:**
- Diseño basado en dominio (DDD)
- Modelado E-R, normalización, modelado dimensional
- Estrategias de sharding y particionamiento
- SQL vs NoSQL, persistencia polglota, patrones CQRS
- Event sourcing y arquitectura event-driven

**Patrones de arquitectura:**
- Base de datos única para monolitos
- Base de datos por servicio para microservicios
- Event sourcing con logs inmutables
- CQRS para separación de comandos y queries

**Salida:**
- Diagramas de arquitectura completos
- Esquemas de base de datos con constraints
- Documentación de flujo de datos
- Estrategias de migración
- Código de ejemplo con patrones implementados

**Herramientas:** Read, Write, Edit, Bash

---

### 5. ⚡ database-optimizer

**Modelo**: N/A | **Activación**: Bajo demanda

Optimización de plataformas de datos incluyendo SQL/NoSQL, sistemas de caché y data pipelines.

**Cuándo se usa:**
- APIs lentas o queries con bajo rendimiento
- Diseño de pipelines de datos escalables
- Integración de datos cross-platform
- Optimización de cache

**Áreas de responsabilidad:**
- Optimización de queries (SQL/NoSQL)
- Tuning de rendimiento (I/O, CPU, memoria)
- Diseño de esquemas e índices
- Integración cross-platform
- Monitoreo y análisis
- Escalabilidad y tolerancia a fallos

**Tecnologías:**
- SQL: PostgreSQL, MySQL, SQL Server, Oracle
- NoSQL: MongoDB, Cassandra, DynamoDB
- Cache: Redis, Memcached
- Pipelines: Kafka, Airflow, Spark, Flink
- Analytics: Snowflake, BigQuery, Redshift
- Search: Elasticsearch, Solr

**Targets de rendimiento:**
- Query latency: <100ms para 95% de queries
- Throughput: >10,000 queries/segundo
- Cache hit rate: >90%
- Pipeline latency: <1s para procesamiento real-time
- Uptime: 99.99% con failover

**Herramientas:** Write, Read, MultiEdit, Bash, Grep

---

### 6. 🔄 data-engineer

**Modelo**: Sonnet | **Activación**: Proactiva

Especialista en pipelines de datos e infraestructura de analytics.

**Cuándo se usa:**
- Pipelines ETL/ELT
- Data warehouses
- Arquitecturas de streaming
- Optimización de Spark
- Diseño de plataformas de datos

**Áreas de enfoque:**
- Diseño de pipelines ETL/ELT con Airflow
- Optimización de jobs Spark y particionamiento
- Streaming de datos con Kafka/Kinesis
- Modelado de data warehouse (esquemas star/snowflake)
- Monitoreo y validación de calidad de datos
- Optimización de costos para servicios cloud de datos

**Salida:**
- DAG de Airflow con manejo de errores
- Job de Spark con técnicas de optimización
- Diseño de esquema de data warehouse
- Implementación de checks de calidad de datos
- Configuración de monitoreo y alertas
- Estimación de costos por volumen de datos

**Herramientas:** Read, Write, Edit, Bash

---

### 7. 💡 prompt-engineer

**Modelo**: Opus | **Activación**: Proactiva

Experto en optimización de prompts para LLMs y sistemas de IA.

**Cuándo se usa:**
- Construcción de features de IA
- Mejora de rendimiento de agentes
- Creación de prompts de sistema

**Expertise:**
- Few-shot vs zero-shot
- Chain-of-thought reasoning
- Role-playing y configuración de perspectiva
- Especificación de formato de salida
- Constitutional AI principles
- Prompting recursivo
- Tree of thoughts
- Prompt chaining y pipelines

**Optimización por modelo:**
- Claude: Énfasis en helpful, harmless, honest
- GPT: Estructura clara y ejemplos
- Modelos open: Necesidades específicas de formato
- Modelos especializados: Adaptación de dominio

**Formato de salida requerido:**

```
### The Prompt
[Texto completo del prompt]

### Implementation Notes
- Técnicas clave usadas
- Por qué se hicieron estas elecciones
- Resultados esperados
```

**IMPORTANTE:** Siempre muestra el prompt completo, nunca solo lo describas.

**Herramientas:** Read, Write, Edit

---

### 8. 🔎 search-specialist

**Modelo**: Haiku | **Activación**: Proactiva

Investigador web experto usando técnicas avanzadas de búsqueda y síntesis.

**Cuándo se usa:**
- Investigación profunda
- Recopilación de información
- Análisis de tendencias
- Análisis competitivo
- Fact-checking

**Áreas de enfoque:**
- Formulación de queries de búsqueda avanzadas
- Búsqueda y filtrado específico de dominio
- Evaluación y ranking de calidad de resultados
- Síntesis de información de múltiples fuentes
- Verificación de hechos y cross-referencing
- Análisis histórico y de tendencias

**Estrategias de búsqueda:**
- Usar frases específicas entre comillas para matches exactos
- Excluir términos irrelevantes con palabras negativas
- Targetear timeframes específicos
- Formular múltiples variaciones de queries
- Filtrado por dominios confiables
- Fuentes académicas para tópicos de investigación

**Salida:**
- Metodología de investigación y queries usadas
- Hallazgos curados con URLs de fuentes
- Assessment de credibilidad de fuentes
- Síntesis destacando insights clave
- Contradicciones o gaps identificados
- Tablas de datos o resúmenes estructurados
- Recomendaciones para investigación adicional

**Herramientas:** WebSearch, WebFetch

---

### 9. ✍️ technical-writer

**Modelo**: Sonnet | **Activación**: Proactiva

Especialista en escritura técnica y creación de contenido.

**Cuándo se usa:**
- Guías de usuario
- Tutoriales
- Archivos README
- Documentación de arquitectura
- Mejorar claridad y accesibilidad del contenido

**Áreas de enfoque:**
- Guías de usuario y tutoriales paso a paso
- Archivos README y documentación de getting started
- Documentación de arquitectura y diseño
- Comentarios de código y documentación inline
- Accesibilidad de contenido y principios de lenguaje plano
- Arquitectura de información y organización de contenido

**Approach:**
1. Escribe para tu audiencia - conoce su nivel de habilidad
2. Lidera con el resultado - ¿qué lograrán?
3. Usa voz activa y lenguaje claro y conciso
4. Incluye ejemplos reales y escenarios prácticos
5. Prueba las instrucciones siguiéndolas exactamente
6. Estructura el contenido con headings claros y flujo

**Salida:**
- Guías de usuario comprehensivas con navegación
- Templates de README con badges y secciones
- Series de tutoriales con complejidad progresiva
- Architecture Decision Records (ADRs)
- Estándares de documentación de código
- Guía de estilo de contenido y convenciones de escritura

**Herramientas:** Read, Write, Edit, Grep

---

## Cómo Funcionan

### Activación Automática

Algunos agentes tienen `description` con la frase **"Use PROACTIVELY"**. Esto significa que Claude Code los invoca automáticamente cuando detecta tareas relevantes:

```yaml
---
name: code-reviewer
description: Expert code review specialist... Use PROACTIVELY after writing or modifying code...
---
```

### Invocación Manual

Puedes invocar cualquier agente manualmente mencionándolo en tu mensaje:

```
"Usa el agente database-architect para diseñar el esquema"
"Quiero que el prompt-engineer mejore este prompt"
```

### Selección de Modelo

Cada agente especifica su modelo óptimo:

- **Opus**: Tareas complejas que requieren máximo razonamiento (database-architect, prompt-engineer)
- **Sonnet**: Balance entre capacidad y velocidad (code-reviewer, python-pro, data-engineer, technical-writer)
- **Haiku**: Tareas rápidas y directas (api-documenter, search-specialist)

## Instalación

```bash
# Windows
xcopy agents %USERPROFILE%\.claude\agents\ /E /I

# Linux/macOS
cp -r agents ~/.claude/agents/
```

## Personalización

Cada archivo `.md` tiene frontmatter YAML con configuración:

```yaml
---
name: mi-agente                    # Nombre único
description: Descripción corta     # Cuándo usarlo
tools: Read, Write, Edit, Bash     # Herramientas disponibles
model: sonnet                      # Modelo a usar (opus/sonnet/haiku)
---
```

Puedes:
1. Modificar descripciones para ajustar cuándo se activan
2. Cambiar herramientas disponibles
3. Actualizar el modelo asignado
4. Personalizar las instrucciones del agente

### Ejemplo de Personalización

```yaml
---
name: code-reviewer
description: Expert code review specialist. Use PROACTIVELY after writing Python code.
tools: Read, Write, Edit, Bash, Grep
model: opus  # Cambiado a opus para análisis más profundo
---

Enfócate especialmente en:
- Seguridad en aplicaciones web
- Optimización de rendimiento
- Patrones de arquitectura hexagonal
```

## Mejores Prácticas

1. **Mantén los agentes enfocados**: Un agente, un dominio
2. **Usa activación proactiva con moderación**: Solo para agentes que realmente deben ejecutarse automáticamente
3. **Asigna modelos apropiados**: Haiku para tareas rápidas, Opus para complejidad
4. **Documenta personalizaciones**: Mantén notas de por qué hiciste cambios
5. **Prueba después de modificar**: Asegúrate de que los agentes funcionan como esperas

## Troubleshooting

### El agente no se activa automáticamente

- Verifica que la `description` incluya "Use PROACTIVELY"
- Asegúrate de que el archivo esté en `~/.claude/agents/`
- Revisa que el frontmatter YAML sea válido

### El agente usa el modelo incorrecto

- Verifica el campo `model:` en el frontmatter
- Opciones válidas: `opus`, `sonnet`, `haiku`

### El agente no tiene acceso a una herramienta

- Agrega la herramienta al campo `tools:` en el frontmatter
- Herramientas disponibles: Read, Write, Edit, Bash, Grep, MultiEdit, Task, WebSearch, WebFetch

---

Para más información sobre configuración general, ver [../README.md](../README.md).
