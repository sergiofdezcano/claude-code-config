# Comandos Personalizados

Slash commands personalizados para Claude Code.

## Comandos Disponibles

### /documentation-generator

Genera documentación comprehensiva para código y APIs.

**Uso**:
```
/documentation-generator
```

**Qué hace**:
- Genera documentación de funciones con parámetros y valores de retorno
- Incluye ejemplos de uso y patrones comunes
- Documenta edge cases y manejo de errores
- Crea documentación de APIs con endpoints y schemas
- Genera guías de instalación y troubleshooting

**Tags**: `documentation`, `api-docs`

**Ejemplo**:
```
Usuario: /documentation-generator para mi API REST
Claude: [Genera documentación completa con endpoints, ejemplos, schemas, etc.]
```

## Cómo Funcionan los Slash Commands

Los slash commands son prompts pre-definidos que se expanden cuando los invocas.

### Formato de Archivo

Cada comando es un archivo Markdown con frontmatter YAML:

```yaml
---
description: Breve descripción del comando
tags: [tag1, tag2]
---

# Título del Comando

Contenido del prompt que se expandirá cuando uses el comando.
```

### Crear un Nuevo Comando

1. Crea un archivo `.md` en esta carpeta:
```
commands/mi-comando.md
```

2. Agrega frontmatter:
```yaml
---
description: Descripción corta de lo que hace
tags: [categoría, tipo]
---

# Mi Comando

Instrucciones detalladas de lo que quieres que Claude haga...
```

3. Úsalo en Claude Code:
```
/mi-comando
```

### Ejemplos de Comandos Útiles

#### Code Review Command
```yaml
---
description: Revisa código con checklist de seguridad y calidad
tags: [review, security]
---

# Code Review

Revisa el código proporcionado enfocándote en:
- Seguridad y vulnerabilidades
- Performance y optimizaciones
- Calidad y mantenibilidad
- Tests y cobertura
```

#### Refactor Command
```yaml
---
description: Refactoriza código aplicando mejores prácticas
tags: [refactor, clean-code]
---

# Refactor Code

Refactoriza el código manteniendo la funcionalidad pero mejorando:
- Legibilidad y nombres descriptivos
- Eliminación de código duplicado
- Aplicación de patrones de diseño
- Separación de concerns
```

## Instalación

```bash
# Windows
xcopy commands %USERPROFILE%\.claude\commands\ /E /I

# Linux/macOS
cp -r commands/* ~/.claude/commands/
```

## Mejores Prácticas

1. **Nombres Descriptivos**: Usa nombres claros para tus comandos
2. **Descripciones Concisas**: El frontmatter debe ser breve pero informativo
3. **Tags Útiles**: Agrupa comandos relacionados con tags
4. **Prompts Detallados**: Sé específico en las instrucciones
5. **Ejemplos**: Incluye ejemplos cuando sea útil

## Troubleshooting

### El comando no aparece

Verifica:
- El archivo está en `~/.claude/commands/`
- El archivo tiene extensión `.md`
- El frontmatter YAML es válido
- Reinicia Claude Code

### El comando se expande pero no hace lo esperado

- Revisa el contenido del prompt
- Asegúrate de que las instrucciones sean claras
- Prueba con ejemplos específicos
- Itera y mejora el prompt

---

Ver [../README.md](../README.md) para más información sobre la configuración completa.
