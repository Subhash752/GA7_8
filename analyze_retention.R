
# Customer Retention Analysis in R

# Quarterly data
quarters <- c("Q1", "Q2", "Q3", "Q4")
retention <- c(69.76, 73.75, 72.39, 73.19)
average <- mean(retention)
industry_target <- 85

# Print summary
cat("Customer Retention Analysis 2024\n")
cat("Quarterly Data:\n")
for (i in 1:4) {
  cat(quarters[i], ":", retention[i], "%\n")
}
cat("Average Retention Rate:", round(average, 2), "%\n")
cat("Industry Target:", industry_target, "%\n")

# Visualization
png("retention_analysis.png", width=800, height=600)
barplot(retention,
        names.arg=quarters,
        col="skyblue",
        ylim=c(0,100),
        main="Customer Retention Rate - 2024",
        ylab="Retention Rate (%)")
abline(h=industry_target, col="red", lwd=2, lty=2)
text(x=1:4, y=retention+2, labels=retention)
dev.off()
