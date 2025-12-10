# 🧪 Casos de Uso para Pruebas del Sistema RAG - Finanzas Cuantitativas

## Dominio: Finanzas Cuantitativas, Pricing de Activos y Riesgo Financiero

---

## INTENCIÓN: SEARCH (Búsqueda de información específica)

### Caso 1: Conceptos Fundamentales
**Prompt:** ¿Qué es el modelo de Fama-French y cuáles son sus factores?

**Objetivo:** Verificar que el sistema busca definiciones precisas y cita fuentes académicas.

---

### Caso 2: Modelos de Valoración
**Prompt:** ¿Cómo se valora un credit default swap (CDS)?

**Objetivo:** Comprobar recuperación de información técnica sobre derivados.

---

### Caso 3: Riesgo de Mercado
**Prompt:** ¿Qué es el Value at Risk (VaR) y cómo se calcula?

**Objetivo:** Evaluar capacidad de explicar metodologías cuantitativas.

---

### Caso 4: Machine Learning en Finanzas
**Prompt:** ¿Qué aplicaciones tiene el Machine Learning en la industria de servicios financieros?

**Objetivo:** Verificar que recupera información sobre IA/ML en finanzas.

---

### Caso 5: Riesgo de Liquidez
**Prompt:** ¿Cómo afecta el riesgo de liquidez al pricing de activos?

**Objetivo:** Comprobar que relaciona conceptos complejos entre documentos.

---

## INTENCIÓN: SUMMARY (Resúmenes)

### Caso 6: Resumen de Documento Específico
**Prompt:** Resume el documento sobre "A Primer on Artificial Intelligence and Machine Learning for the Financial Services Industry"

**Objetivo:** Verificar que identifica y resume un documento específico por nombre.

---

### Caso 7: Resumen Temático
**Prompt:** Resume los principales conceptos sobre modelos de pricing de activos

**Objetivo:** Evaluar capacidad de sintetizar información de múltiples fuentes.

---

### Caso 8: Resumen de Metodologías
**Prompt:** Resume las metodologías cuantitativas para la gestión de riesgo crediticio

**Objetivo:** Comprobar síntesis de contenido técnico especializado.

---

### Caso 9: Resumen Histórico
**Prompt:** Resume la evolución de los modelos de valoración de opciones

**Objetivo:** Verificar que sintetiza información histórica o evolutiva.

---

## INTENCIÓN: COMPARISON (Comparaciones)

### Caso 10: Comparación de Riesgos
**Prompt:** Compara el riesgo de crédito versus el riesgo de mercado

**Objetivo:** Evaluar capacidad de contrastar conceptos diferentes.

---

### Caso 11: Comparación de Modelos
**Prompt:** Compara el modelo CAPM con el modelo APT (Arbitrage Pricing Theory)

**Objetivo:** Verificar comparación de modelos financieros clásicos.

---

### Caso 12: Comparación de Metodologías
**Prompt:** Compara los métodos de Monte Carlo versus simulación histórica para el cálculo de VaR

**Objetivo:** Evaluar contraste de técnicas cuantitativas.

---

## INTENCIÓN: GENERAL (Conocimiento general - sin RAG)

### Caso 13: Saludo/Conversación
**Prompt:** Hola, ¿cómo estás?

**Objetivo:** Verificar que el sistema responde apropiadamente sin buscar en documentos.

---

### Caso 14: Pregunta Fuera del Dominio
**Prompt:** ¿Cuál es la capital de Francia?

**Objetivo:** Comprobar que el sistema distingue queries fuera del dominio financiero.

---

### Caso 15: Consulta Meta
**Prompt:** ¿Sobre qué temas puedes ayudarme?

**Objetivo:** Evaluar que el sistema explica sus capacidades sin acceder al vector store.

---

## CASOS ADICIONALES (Opcional - Validación Robusta)

### Caso 16: Query Ambigua
**Prompt:** ¿Qué es el beta?

**Objetivo:** Verificar cómo maneja términos con múltiples significados en finanzas.

---

### Caso 17: Pregunta Multifacética
**Prompt:** ¿Cómo se relacionan la volatilidad implícita, el pricing de opciones y el modelo Black-Scholes?

**Objetivo:** Evaluar capacidad de integrar conceptos interrelacionados.

---

## 📊 MATRIZ DE COBERTURA

| Intención | Casos | % Cobertura |
|-----------|-------|-------------|
| SEARCH | 5 | 33% |
| SUMMARY | 4 | 27% |
| COMPARISON | 3 | 20% |
| GENERAL | 3 | 20% |
| **TOTAL** | **15** | **100%** |

---

## 🎯 MÉTRICAS A EVALUAR EN CADA CASO

1. **Clasificación correcta** de intención
2. **Documentos recuperados** (nombres en logs)
3. **Número de fragmentos** usados
4. **Calidad de citas** (¿menciona fuentes?)
5. **Aprobación del evaluador** (APROBADO/RECHAZADO)
6. **Tiempo de respuesta**
7. **Coherencia** de la respuesta

---

## 📝 FORMATO PARA DOCUMENTAR EN INFORME

Para cada caso de uso, registrar:

```
Caso X: [Título]
Prompt: "[query exacta]"
Intención detectada: [search/summary/comparison/general]
Documentos usados: [nombre1, nombre2, ...]
Fragmentos recuperados: [N]
Evaluación: [APROBADO/RECHAZADO]
Tiempo: [X.XX] segundos
Respuesta (resumen): [primeras 100 palabras...]
```

---

## ⚠️ NOTA SOBRE RATE LIMITS

Si encuentras errores de rate limit de Groq (429):
- **Solución inmediata:** Espera 5-10 minutos entre queries
- **Distribución:** Prueba 3-4 casos, descansa, continúa
- **Alternativa:** Considera ejecutar casos en días diferentes para el free tier
