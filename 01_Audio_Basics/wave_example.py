# Audio signal parameters
# - Number of channels (this one usually be 1 (Mono) or 2 (Sterio))
# - Sample width
# - FrameRate / SampleRate => most common rate is 44.1 KHz
# - Number of frames
# - Value of a frame

##########################################################################################
##########################################################################################


import wave

# Open wave file
obj = wave.open("Youssef.wav", "rb")  # rb stands for read binary mode

# Get file info with the getters
print("Number of channels: ", obj.getnchannels())
print("Sample width: ", obj.getsampwidth())
print("Frame rate: ", obj.getframerate())
print("Number of frames: ", obj.getnframes())
print("Parameters: ", obj.getparams())

TimeInSec = obj.getnframes()/obj.getframerate()
print(TimeInSec)

frames = obj.readframes(-1) # (-1) should read all frames
print(type(frames), type(frames[2])) # should be 'bytes' , 'int'

# Get length of the frames
print(len(frames)) # this number is the total length of frames in 2 channels with 2 sample width

# The file should be closed
obj.close()


##########################################################################################
##########################################################################################

# Set file info to another file (copy wav file)

# new_obj = wave.open("NewYoussef(copy).wav", "wb")  # wb stands for write binary mode

# # Set data by setters 
# new_obj.setnchannels(2)
# new_obj.setsampwidth(2)
# new_obj.setframerate(8000)

# new_obj.writeframes(frames)

# new_obj.close()