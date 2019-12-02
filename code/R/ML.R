#install.packages("ggplot2", dependencies=c("Depends", "Suggests"))
#install.packages("caret", dependencies=c("Depends", "Suggests"))
library(caret)
# attach the iris dataset to the environment
data(iris)
# rename the dataset
dataset <- iris

# Load the Caret package which allows us to partition the data
# We use the dataset to create a partition (80% training 20% testing)
index <- 120
# select 20% of the data for testing
testset <- iris[-index,]
# select 80% of data to train the models
trainset <- iris[index,]
# Build the model
library(class)
iris_pred <- svmLinear3(train = trainset, test = testset, cl = iris.trainLabels, k=3)
## simple example
data(iris)

lir <- lssvm(Species~.,data=iris)

lir

lirr <- lssvm(Species~.,data= iris, reduced = FALSE)

lirr
