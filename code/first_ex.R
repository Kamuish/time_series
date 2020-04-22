setwd("/home/amiguel/phd/classes/time_series/project")

library(astsa)             # then load it (has to be done at the start of each session)

####################################################
# store the data set as a CSV
ts2csv <- function(x) {
  fname <- paste0(deparse(substitute(x)), ".csv")
  readr::write_csv(tsibble::as_tsibble(x, gather = FALSE), fname)
}
ts2csv(sunspotz)
####################################################

sun_spots <- sunspotz
plot(sun_spots)
par(mfrow=c(1,1))

write.csv(sun_spots, file = 'teste')
spec_raw <- spec.pgram(sun_spots, log="no", main="", sub="", taper = 0)
#spec.pgram(sun_spots, spans=10, log="no", main="", sub="")
max_index <- which.max(spec_raw$spec)
df <- cbind(spec_raw$freq, spec_raw$spec)
write.csv(df, file='data_kernels/kernel_raw')


print("==> NUMBER 1 -> POWER + CONFIDENCE INTERVALS")
spec_raw$spec[max_index]
2*spec_raw$spec[max_index] / qchisq(c(0.025,0.975),2)
2*spec_raw$spec[max_index] / qchisq(c(0.05,0.95),2)




print("==> NUMBER 1 -> Freq + period")

print("Frequency of the max power:")
spec_raw$freq[max_index]
print("Period of: ")
print(1/spec_raw$freq[max_index])



print("==> NUMBER 1 -> FILTERED OUTPUTS")

print("==> daniell ")
dan <- spec.pgram(sun_spots, kernel("daniell", 3), log='no')
max_index <- which.max(dan$spec)
#cat("Frequency ", (0.5/dan$freq[max_index]))
print("Frequency of the max power:")
dan$freq[max_index]
print("Period of: ")
print(1/dan$freq[max_index])

df <- cbind(dan$freq, dan$spec)
write.csv(df, file='data_kernels/kernel_dan')



