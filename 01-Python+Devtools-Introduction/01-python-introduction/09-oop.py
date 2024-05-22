# examples for objects and classes in Python

# simple base class
class DataEntryBasic:
  def __init__(self, id) -> None:
    self.id = id
  
  def __str__(self) -> str:
    return f"{self.id}"

# extend it by data and functions
class DataEntry(DataEntryBasic):
  def __init__(self, id, kind, measurementDatetime, value) -> None:
    super().__init__(id)
    self.kind = kind
    self.measurementDatetime = measurementDatetime
    self.value = value

  def __str__(self) -> str:
    return f"{super().__str__()} {self.kind} {self.measurementDatetime}:{self.value}"
  
  def getMeasurement(self):
    return [self.measurementDatetime, self.value]
  
  def addLocation(self, id, latitude, longitude) -> None:
    self.location = LocationInfo(id, latitude, longitude)
  
class LocationInfo:
  def __init__(self, id, latitude, longitude) -> None:
    self.id = id
    self.latitude = latitude
    self.longitude = longitude

dt1 = DataEntry(1,"Air","2024-04-29T09:31:42.938Z",14.3)
dt2 = DataEntry(2,"Air","2024-04-29T09:31:42.985Z",14.7)
dt3 = DataEntry(3,"Air","2024-04-29T09:31:43.063Z",15.9)

entries = []
entries.append(dt1)
entries.append(dt2)
entries.append(dt3)

# check if default instance print looks nice
for e in entries:
  print(e)

# call an object function
for e in entries:
  print(e.getMeasurement())

# create association
dt1.addLocation("220735110",60.0495,17.62248)
