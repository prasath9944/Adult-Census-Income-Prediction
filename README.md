<h1>Adult Census Income Prediction</h1>

<br>
<table>
  <tr>
    <th>Project Title</th>
    <td>Adult Census Income Prediction</th>
  </tr>
  <tr>
    <th>Technologies</th>
    <td>Machine Learning Technology</td>
  </tr>
  <tr>
    <th>Domain</th>
    <td>Finance</td>
  </tr>
    <tr>
    <th>Project Difficulties level</th>
    <td>Intermediate</td>
  </tr>
</table>
<hr>

The Goal is to predict whether a person has an income of more than 50K a year or not. This is basically a binary classification problem where a person is classified into the >50K group or <=50K group.




## Acknowledgements

 - [Dataset](https://www.kaggle.com/datasets/overload10/adult-census-dataset)
 - [scikit](https://scikit-learn.org/stable/index.html)
 - [flask](https://flask.palletsprojects.com/en/2.2.x/)
 - [pandas](https://pandas.pydata.org/docs/)
 - [numpy](https://numpy.org/doc/)
 - [Scaling Up the Accuracy of Naive-Bayes Classifiers: a Decision-Tree Hybrid](http://robotics.stanford.edu/~ronnyk/nbtree.pdf)
 


## API Reference

#### Training Pipeline

```http
  /trainingpipeline
```

#### Get and Post home page

```http
  GET /
  GET/home
```
#### Post Predict page

```http
  POST/predict
```
## About Dataset
This data was extracted from the 1994 Census bureau database by Ronny Kohavi and Barry Becker (Data Mining and Visualization, Silicon Graphics). A set of reasonably clean records was extracted using the following conditions: ((AAGE>16) && (AGI>100) && (AFNLWGT>1) && (HRSWK>0)). The prediction task is to determine whether a person makes over $50K a year.

### Description of fnlwgt (final weight)
The weights on the Current Population Survey (CPS) files are controlled to independent estimates of the civilian noninstitutional population of the US. These are prepared monthly for us by Population Division here at the Census Bureau. We use 3 sets of controls. These are:

- A single cell estimate of the population 16+ for each state.

- Controls for Hispanic Origin by age and sex.

- Controls by Race, age and sex.

We use all three sets of controls in our weighting program and "rake" through them 6 times so that by the end we come back to all the controls we used. The term estimate refers to population totals derived from CPS by creating "weighted tallies" of any specified socio-economic characteristics of the population. People with similar demographic characteristics should have similar weights. There is one important caveat to remember about this statement. That is that since the CPS sample is actually a collection of 51 state samples, each with its own probability of selection, the statement only applies within state.


## Authors

- [@prasath](https://github.com/prasath9944)


## Screenshots
#### Home Page

![HomePage1](https://github.com/prasath9944/Adult-Census-Income-Prediction/blob/main/Images/homepage.jpg)

![Home Page1](https://github.com/prasath9944/Adult-Census-Income-Prediction/blob/main/Images/homepage2.jpg)
#### Predict Page

![Predict Page](https://github.com/prasath9944/Adult-Census-Income-Prediction/blob/main/Images/predictpage.jpg)




## Running Tests

To run Application, run the following command

```bash
  pip install -r requirements.txt
```
```bash
  python app.py
```

## Deployment

To deploy this project run
```bash
  docker build -d -t census .
```
```bash
  docker run -p 8080:8080 census
```
```bash
  git add .
```
```bash
  git commit -m "Message"
```
```bash
  git push origin main
```



## Features

- age
- workclass
- fnlwgt
- education
- education-num
- marital-status
- occupation
- relationship
- race
- sex
- capital-gain
- capital-loss
- hours-per-week
- country
- salary




## Tech Stack

**Client:** Html,Css,Bootstrap

**Server:** Python, Flask


## Demo

![Demo](https://github.com/prasath9944/Adult-Census-Income-Prediction/blob/main/Images/CensusIncome.gif)

## 🚀 About Me
- 👋 Hi, I’m Prasath K Working as a Full Stack Dotnet Developer in @Cognizant at Chennai,India.
- I’m interested in Artificial Intelligence,Data Science and I would love to explore more on data Domain.

## 🔗 Links

[Application Hosted](http://ec2-13-233-109-20.ap-south-1.compute.amazonaws.com:8080/home)

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/prasath-k-084a46204/)

[![Github](https://www.iconpacks.net/icons/3/free-github-logo-icon-6531.png)](https://github.com/prasath9944)
