# Code from https://www.r-bloggers.com/visualizing-neural-networks-in-r-update/

library('clusterGeneration')
library('nnet')

seed.val<-2
set.seed(seed.val)

num.vars<-8
num.obs<-1000

#input variables
cov.mat<-genPositiveDefMat(num.vars,covMethod=c("unifcorrmat"))$Sigma
rand.vars<-mvrnorm(num.obs,rep(0,num.vars),Sigma=cov.mat)

#output variables
parms<-runif(num.vars,-10,10)
y1<-rand.vars %*% matrix(parms) + rnorm(num.obs,sd=20)
parms2<-runif(num.vars,-10,10)
y2<-rand.vars %*% matrix(parms2) + rnorm(num.obs,sd=20)

#final datasets
rand.vars<-data.frame(rand.vars)
resp<-data.frame(y1)
names(resp)<-c('Y1')
dat.in<-data.frame(resp,rand.vars)


#nnet function from nnet package
library(nnet)
set.seed(seed.val)
mod1<-nnet(rand.vars,resp,data=dat.in,size=10,linout=T)

#neuralnet function from neuralnet package, notice use of only one response
library('neuralnet')
form.in<-as.formula('Y1~X1+X2+X3+X4+X5+X6+X7+X8')
set.seed(seed.val)
mod2<-neuralnet(form.in,data=dat.in,hidden=10)

#mlp function from RSNNS package
library('RSNNS')
set.seed(seed.val)
mod3<-mlp(rand.vars, resp, size=10,linOut=T)


#import the function from Github
library(devtools)
source_url('https://gist.github.com/fawda123/7471137/raw/cd6e6a0b0bdb4e065c597e52165e5ac887f5fe95/nnet_plot_update.r')

#plot each model
plot.nnet(mod1)
plot.nnet(mod2)
plot.nnet(mod3)


svg("nnet_ex.svg", width = 12, height = 10)
plot.nnet(mod1)
dev.off()

system("inkscape --file=nnet_ex.svg --export-area-drawing --without-gui --export-pdf=nnet_ex.pdf")


png("nnet_ex.png", width = 600, height = 480)
plot.nnet(mod1)
dev.off()

x <- seq(-5, 5, length.out = 100)

tanh(x)


png("activation_ex.png", width = 300, height = 240)
plot(x, tanh(x), type = 'l', lwd = 2)
abline(h = 0)
abline(v = 0)
dev.off()


