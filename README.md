# Generadores de Grafos y Análisis Topológico

Este repositorio contiene la implementación en Python de seis modelos clásicos de generación de grafos. El proyecto incluye la lógica algorítmica para la creación de los grafos y su exportación para visualización y análisis estructural.

Este trabajo fue desarrollado como parte de la materia "Diseño y Análisis de Algoritmos" en los estudios de la Maestría MCIC en el Centro de Investigación en Computación (CIC-IPN).

## 🚀 Modelos Implementados

El código principal genera topologías basadas en los siguientes algoritmos:
1. **Modelo de Malla**
2. **Modelo de Erdős-Rényi**
3. **Modelo de Gilbert**
4. **Modelo Geográfico simple**
5. **Modelo de Barabási-Albert**
6. **Modelo de Dorogovtsev-Mendes**

## 📂 Estructura del Proyecto

El repositorio está organizado de la siguiente manera:

- `grafos.py`: Script principal que contiene las clases `Nodo`, `Arista` y los métodos generadores para cada uno de los seis modelos.
- **Carpetas por método:** Cada algoritmo tiene su propio subdirectorio, el cual contiene:
- `*.gv`: Archivos exportados con la topología de la red (formatos de 50, 200 y 500 nodos).
- `*.png`: Renderizados finales de los grafos utilizando Gephi, aplicando algoritmos de distribución geométrica como Yifan Hu Proporcional para evidenciar sus propiedades estructurales (agrupamiento, hubs, etc.).

## 🛠️ Tecnologías y Herramientas

* **Lenguaje:** Python
* **Visualización y renderizado:** Gephi

## 👤 Autor

**Antonio Baldo**
