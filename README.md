# Projects
* Uploaded heart disease data from UCI Machine Learning Repository [[1]](https://archive.ics.uci.edu/ml/datasets/Heart+Disease).
* Used k-fold cross validation to choose the parameter K of K-Nearest Neighbors.
* Applied KNN algorithm to distinguish whether heart disease is present in a specific patient.
* Visualized results using Matplotlib and Seaborn.

# Code and Resources Used
* Python Version: 3.7
* Packages: pandas, numpy, sklearn, matplotlib, seaborn.
# Classification results
The cleveland heart disease dataset includes 14 different physiological attributes that can indicate the existence of heart disease, these attributes are:
* age
* sex
* chest pain type (4 values)
* resting blood pressure
* serum cholestoral in mg/dl
* fasting blood sugar 
* resting electrocardiographic results (values 0,1,2)
* maximum heart rate achieved
* exercise induced angina
* oldpeak = ST depression induced by exercise relative to rest
* the slope of the peak exercise ST segment
* number of major vessels (0-3) colored by flourosopy
* thal: 3 = normal; 6 = fixed defect; 7 = reversable defect
* Target: 0 = neagtive; 1 = positive

Using the k-fold cross validation algorithm I chose the paramter k of the k_nearest algorithm as k=19. This yields the following results:

![Classification Report](https://user-images.githubusercontent.com/82426428/133906979-5238a753-7d45-4aea-904a-47f185016c69.PNG)
# Data Visualization
I used Seaborn libraray to plot different pairwise attributes in the testing dataset, especially the age, chest pain type, resting blood pressure, serum cholestoral, maximum heart rate achieved and the oldpeak [download]. ALso, I created an interactive plot to illustrate the relation between maximum heart rate achieved, resting blood pressure and the serum cholestoral in mg/dl [Capture44](https://github.com/YoussefAithaddou/Projects/blob/main/Capture454.PNG).
![download](https://user-images.githubusercontent.com/82426428/133907210-da1d4ec0-dee6-4e2d-bf51-948c9c24c518.png)

![Capture44](https://user-images.githubusercontent.com/82426428/133907259-2fe06d8b-661b-4d10-909f-49f8baadeddd.PNG)
