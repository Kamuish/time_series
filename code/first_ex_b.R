
require(biwavelet)
library(astsa)

data.data = astsa::sunspotz

data.time = seq(1749,1978, 0.5)


# Compare non-corrected vs. corrected wavelet spectrum
wt1=wt(cbind(data.time, data.data))
par(mfrow=c(2,1))
par(oma=c(0, 0, 0, 1), mar=c(5, 4, 4, 5) + 0.1)

plot(wt1, type="power.corr.norm", main="Bias-corrected",plot.cb=TRUE, alpha.coi=0.7)
plot(wt1, type="power.norm", main="Not-corrected",plot.cb=TRUE, alpha.coi=0.7)
