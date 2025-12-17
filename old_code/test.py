results = model("https://ultralytics.com/images/bus.jpg")

# Access the first result object
result = results[0]

# Now you can call show() or save()
result.show()
result.save("predicted_output.jpg")

# You can also print details
print(result.names)
print(result)
