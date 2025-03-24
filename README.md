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

## 🕁️ Instrucciones de uso en Python (local)

1. Clona el repositorio y crea un entorno virtual:

```bash
git clone https://github.com/tu_usuario/rag-bmw-m235i.git
cd rag-bmw-m235i
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

2. Instala las dependencias:

```bash
pip install -r requirements.txt
```

3. Exporta tus claves como variables de entorno:

```bash
export OPENAI_API_KEY="tu_clave_openai"
export PINECONE_API_KEY="tu_clave_pinecone"
export LANGSMITH_API_KEY="tu_clave_langsmith"  # opcional
```

4. Ejecuta el archivo principal (adaptado desde el notebook):

```bash
python main.py
```

5. Escribe preguntas en consola o modifica el archivo para pruebas automáticas.


---

## 📂 Estructura del Colab

```text
lab09.ipynb
🔻— Instala dependencias
🔻— Configura claves
🔻— Inicializa modelo LLM y embeddings
🔻— Conecta con Pinecone
🔻— Carga y divide contenido web
🔻— Indexa en Pinecone
🔻— Define flujo RAG
🔻— Ejecuta preguntas
```

## 📂 Pruebas
![image](https://github.com/user-attachments/assets/56768348-a5f3-40f4-8c48-9fe03ee7b5ee)
![image](https://github.com/user-attachments/assets/4dbd9d0f-626d-40a5-b1f8-c20caa46a3f0)
![image](https://github.com/user-attachments/assets/892bbbcc-f40f-4929-ae31-f1a6c75ef0f6)
![image](https://github.com/user-attachments/assets/1c8e64d2-6e49-4764-9a81-b7cb91124761)
![image](https://github.com/user-attachments/assets/4ca6b11a-b5b5-4dec-a43b-e5cf1cb2bfd3)
![image](https://github.com/user-attachments/assets/4c245582-4fc0-48e8-bcb0-87a1d417f028)
![image](https://github.com/user-attachments/assets/3d5a657b-9bb4-47da-a9d3-4d462fa4497e)




---

## ✍️ Autor

**Tomas Suárez Piratova**  
🚀 Proyecto académico para evaluación de LangChain y Pinecone







