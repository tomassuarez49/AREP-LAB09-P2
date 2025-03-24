# 🚗 RAG sobre el BMW M235i con LangChain, Pinecone y OpenAI

Este proyecto implementa una aplicación de **RAG (Retrieval-Augmented Generation)** centrada en un único artículo de prueba sobre el **BMW M235i Coupé**.

Se utiliza contenido real del siguiente artículo:
👉 [extremamotor.es - Prueba BMW M235i](https://extremamotor.es/prueba-bmw-m235i-coupe-326-cv-explosivos/)

## 🧠 ¿Qué hace esta app?

- Extrae el contenido de un artículo web.
- Lo divide en fragmentos útiles (chunks).
- Genera embeddings con **OpenAI**.
- Indexa los datos en **Pinecone**.
- Permite hacerle preguntas al sistema como:
  - ¿Qué potencia tiene el BMW M235i?
  - ¿Qué tipo de tracción tiene?
  - ¿Qué sensaciones transmite el vehículo?

---

## 🏗️ Arquitectura del Proyecto

### 🔹 Componentes principales:

| Componente     | Descripción                                                                 |
|----------------|-----------------------------------------------------------------------------|
| `WebBaseLoader`| Carga el contenido del artículo web seleccionado.                          |
| `RecursiveCharacterTextSplitter` | Divide el texto en fragmentos superpuestos para mejor contexto. |
| `OpenAIEmbeddings` | Convierte los fragmentos en vectores numéricos.                          |
| `PineconeVectorStore` | Almacena y permite búsqueda de esos vectores.                          |
| `LangGraph (StateGraph)` | Define la lógica del flujo RAG: recuperar contexto y generar respuesta. |
| `Prompt`       | Prompt base del hub de LangChain optimizado para RAG.                      |

---

## ⚙️ Requisitos

- Python 3.10+
- Cuenta en OpenAI
- Cuenta en Pinecone
- Cuenta opcional en LangSmith (para trazabilidad)

---

## 🛠️ Instalación y Ejecución en Google Colab

1. Abre el Colab en:  
   📌 [Colab Notebook](https://colab.research.google.com/drive/1VNWbHf7hoeOvcAsem8BoxZ8wNVcHIab7)

2. Ejecuta todas las celdas, e introduce tus claves cuando se te pidan:
   - 🔑 `LANGSMITH_API_KEY`
   - 🔑 `OPENAI_API_KEY`
   - 🔑 `PINECONE_API_KEY`

3. El sistema cargará y procesará el artículo de extremamotor.es

4. Puedes hacerle preguntas como:

```python
"¿Qué marca es el M235i?"
"¿Cuánta potencia tiene?"
"¿Qué tipo de tracción tiene?"
```

---

## 📂 Estructura del Colab

```text
Untitled4.ipynb
🔻— Instala dependencias
🔻— Configura claves
🔻— Inicializa modelo LLM y embeddings
🔻— Conecta con Pinecone
🔻— Carga y divide contenido web
🔻— Indexa en Pinecone
🔻— Define flujo RAG
🔻— Ejecuta preguntas
```

---

## ✍️ Autor

**Tomas Suárez Piratova**  
🚀 Proyecto académico para evaluación de LangChain y Pinecone


