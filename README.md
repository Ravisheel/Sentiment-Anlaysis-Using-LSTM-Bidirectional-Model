# Sentiment-Anlaysis-Using-LSTM-Bidirectional-Model

Text data sentiments analysis. The following model predict on the sentiments of the text and predict whether the given sentence sentiments is [Positive, Neutral, Negative]. I have developed the model from the scratch and build LSTM (Bidirectional) Neural Network which is basically a type of Recurrent Neural Network. Here we are dealing with the sequential data (Text data, Time series data...). Recurrent Neural Networks are good with sequential data becuase it has a loop that allow information to persist over time but we can't use simple RNN because of Vanishing Gradient Descent problem and because of that the weights will not be able to adjust properly during the training in the embedding layers. As with the time goes the information will loose from the normal RNN (i.e.. feedforward neural network) but in the Bidirectional LSTM (it is 2 way 1-> Forward and 1-> Backward) which will help the NN(Neural Network) to remember the old data. Which makes it powerful in remembering the text data. 

Now the question comes how to make our model understand the context present in the sentence. For that I have use GloVe 100 dimension embedding layer which is already trained on 6 BILLION words and every word is representing in 100 dimension. GloVe is developed by researchers at Stanford. There are many word embedding layer Word2Vec, GloVe, Fastext, Elmo and Bert. 


For deployment of this project make sure Flask library is installed open cmd prompt (windows) type. -->  pip install virtualenv
To run the environment 




![image](https://github.com/Ravisheel/Sentiment-Anlaysis-Using-LSTM-Bidirectional-Model/assets/49792350/e59cdf78-400c-4616-a677-14e14d371946)
