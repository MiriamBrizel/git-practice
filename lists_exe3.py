turtle_status = ["sick", "healthy", "healthy", "healthy", "sick", "sick", "healthy", "sick", "healthy", "healthy", "healthy", "healthy", "healthy", "sick"]
num_of_sick = turtle_status.count("sick")
num_of_healthy = turtle_status.count("healthy")
if num_of_sick > num_of_healthy:
    print("We have a shell of a problem")
else:
    print("Let's shell-ebrate")