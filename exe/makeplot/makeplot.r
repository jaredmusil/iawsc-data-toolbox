#making a plot using R


#R --no-save << endip

#postscript(file="$3.ps", horizontal=FALSE,paper="letter",pointsize=10)
pdf(file="plots.pdf",width = 8, height = 11)
par(mfrow=c(3,2))

#=====================Monthly
inp <- read.table("MONTH")

num<-  inp[[1]]
round<-  inp[[2]]
step<- inp[[3]]
year<- inp[[4]]
mth<-  inp[[5]]
obs<-  inp[[6]]
sim<-  inp[[7]]

plot(mth[step==1][num==0],obs[step==1][num==0],type="l",lwd=4,col="black",xlab="All Months",ylab="Monthly Values",main="Solar Radiation",ylim=range(obs[step==1],sim[step==1]))
lines(mth[step==1][num==0],sim[step==1][num==0],type="l",lwd=2,col="cyan")

plot(mth[step==2][num==0],obs[step==2][num==0],type="l",lwd=4,col="black",xlab="All Months",ylab="Monthly Values",main="PET",ylim=range(obs[step==2],sim[step==2]))
lines(mth[step==2][num==0],sim[step==2][num==0],type="l",lwd=2,col="cyan")

plot (num[step==3][num>=1],obs[step==3][num>=1],type="l",lwd=4,col="black",xlab="Month",ylab="Monthly Values",main="Monthly" ,ylim=range(obs[step==3],sim[step==3]))
lines(num[step==3][num>=1],sim[step==3][num>=1],type="l",lwd=2,col="cyan")

#=====================Annual
inp <- read.table("ANNUAL")

round<-  inp[[1]]
step<- inp[[2]]
year<- inp[[3]]
obs<-  inp[[4]]
sim<-  inp[[5]]

plot (year[step==3][year>=1],obs[step==3][year>=1],type="l",lwd=4,col="black",xlab="Year",ylab="Annual Values",main="Annual",ylim=range(obs[step==3],sim[step==3]))
lines(year[step==3][year>=1],sim[step==3][year>=1],type="l",lwd=2,col="green")

#=====================Annual NS
inp <- read.table("NSyear")

round<-  inp[[1]]
step<- inp[[2]]
year<- inp[[3]]
ns<-   inp[[4]]

year<-year[ns>=-10]
step<-step[ns>=-10]
ns  <-  ns[ns>=-10]

plot(year[step==4],ns[step==4],type="p",lwd=7,col="red",xlab="Year",ylab="Nash Sutcliff",main="Nash Sutcliff")

boxplot(ns[step==4],col="red",xlab="All Years",ylab="Nash Sutcliff",main="Nash Sutcliff")


quit()
n
#endip

#gv $3.ps
#lpr -Pmargs NS$1_$1.ps
 #echo
 #echo Program has completed execution
 #echo

