
# **Análisis de la Ejecución de Ingresos Públicos en Brasil 2013-2021**



## **Descripción del Proyecto** 

   - El gobierno de Brasil, a través de sus distintos órganos, gestiona la recaudación de ingresos públicos para financiar los servicios y proyectos que benefician a la sociedad. Cada año, se realiza una planificación detallada para prever cuánto se espera recaudar, pero a menudo la recaudación real difiere de lo previsto debido a diversos factores como la evasión fiscal, fluctuaciones económicas, ineficiencias administrativas, entre otros.

   - Incluye qué técnicas o enfoques se usaron para llevar a cabo el análisis:   Este proyecto realiza un análisis exploratorio de cada una de las base de datos, que tras la normalización, se unen para analizar el conjunto en su totalidad.

   - El presente trabajo consiste en identificar patrones, detectar áreas problemáticas donde la recaudación ha sido consistentemente menor a la previsto en 7 años [2013-2021]



## **Objetivos específicos**

- Encontrar desviaciones entre lo previsto y lo recaudado: Determinar en qué categorías económicas o tipos de ingresos las diferencias son más pronunciadas.

- Evolución temporal de la recaudación: Identificar cómo han cambiado las previsiones y recaudaciones año a año, y si existen patrones temporales, como meses específicos donde hay mayores discrepancias.

- Rendimiento por órgano y unidad gestora: Evaluar qué órganos o unidades gestoras son más eficientes en términos de alcanzar las metas de recaudación y cuáles presentan consistentemente una baja ejecución.


## **Estructura del Proyecto**

        
        ├── data/                # Datos crudos y procesados
        ├── Proyecto_EDA_Brasil/ # Notebooks de Jupyter con el análisis
        ├── src/                 # Scripts de procesamiento y modelado
        ├── results/             # Gráficos y archivos de resultados
        ├── README.md            # Descripción del proyecto
        

## 🛠️ Instalación y Requisitos
        Este proyecto usa Python 3.8 y requiere las siguientes bibliotecas:
        - pandas
        - numpy
        - matplotlib
        - seaborn
        - scikit-learn



## 📊 Resultados y Conclusiones

- Órganos con menor ejecución presupuestaria:

Se identificaron los órganos con los porcentajes más bajos de ejecución presupuestaria. Entre ellos destacan:
      
      - Hospital Cristo Redentor S.A. y Agencia Espacial Brasileña, con un porcentaje de ejecución promedio inferior al 6%.

Estos resultados revelan áreas críticas donde la planeación y ejecución presupuestaria necesitan mejoras sustanciales.

- Órganos con mayor inconsistencia (desviación estándar):

Los órganos con mayor variabilidad en la ejecución a lo largo del tiempo incluyen:
         
         - Ministerio del Medio Ambiente (unidades vinculadas) y Servicio Federal de Procesamiento de Datos.

Esto sugiere que no cuentan con una planificación financiera estable, dificultando la asignación eficiente de recursos.


- Evolución de las variables clave en el tiempo:

Al evaluar las variables Previsión, Real, Diferencia Absoluta, y Porcentaje de Desviación, se observó lo siguiente:

      - Previsión y Real presentan valores relativamente constantes, indicando estabilidad en la planificación de presupuestos totales, pero sin una mejora significativa en los resultados.

      - Porcentaje de Desviación muestra una tendencia uniforme, lo que podría estar relacionado con una falta de ajustes en la metodología de previsión o ejecución.


**Conclusiones**

1. Planificación Presupuestaria Ineficiente en Órganos Clave:

         Los órganos con bajo porcentaje de ejecución y alta inconsistencia evidencian deficiencias en la gestión presupuestaria, ya sea por falta de planeación, ejecución inadecuada o problemas estructurales.

2. Análisis de Tendencias en el Tiempo:

         La estabilidad en los valores de Previsión y Real sugiere que no hay esfuerzos significativos para mejorar la ejecución en el tiempo. Esto puede indicar que no se están realizando ajustes basados en aprendizajes de años anteriores.

3. Propuesta de Mejora:

         - Los órganos con baja ejecución deben ser priorizados para revisar sus planes de acción.
         
         - Implementar métodos de evaluación y ajuste más dinámicos en los procesos de previsión y ejecución podría mejorar la eficiencia presupuestaria.



 ## 🔄 Próximos Pasos
   
   1. Identificación de áreas críticas:
       - Los órganos con menor porcentaje de ejecución deben ser revisados para entender las causas subyacentes (problemas de planeación, asignación de recursos, o ejecución de políticas)  
       - Los órganos con mayor inconsistencia requieren mecanismos de control que reduzcan la variabilidad y permitan una ejecución más predecible.
  

   2. Diseñar estrategias específicas:

      - Implementar medidas de seguimiento y soporte para los órganos con baja ejecución y alta inconsistencia.
      - Fomentar la capacitación y el uso de herramientas tecnológicas que mejoren la precisión de las previsiones y la ejecución de las metas.
        - Refinar el modelo predictivo usando más datos históricos.
        - Implementar técnicas avanzadas de feature engineering para mejorar la precisión.
        

 ## 🤝 Contribuciones
      Las contribuciones son bienvenidas. Si deseas mejorar el proyecto, por favor abre un pull request o una issue.
      
 ## ✒️ Autores
       Marta Blanco - [@marta-ba] (https://github.com/juanperez)
        
