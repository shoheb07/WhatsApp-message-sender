import pywhatkit

# Phone Number with Country Code
phone_number = "+911234567890"

# Message
message = "Hello! This message was sent using Python."

# Time (24-hour format)
hour = 18
minute = 30

# Send WhatsApp Message
pywhatkit.sendwhatmsg(
    phone_number,
    message,
    hour,
    minute
)

print("Message Scheduled Successfully!")
