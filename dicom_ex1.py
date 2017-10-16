import dicom

ds = dicom.read_file('scans/CT_small.dcm')


ds[0x0010,0x1010].value  = 'anonymous'
ds['PatientName']  = 'anonymous'

print ds[0x0010,0x1010].value
print ds.PatientName.value
ds.save_as('output/CT_small_anonymous.dcm')
#

ds = dicom.read_file('output/CT_small_anonymous.dcm')

print ds[0x0010,0x1010].value

for patient_item in ds.dir():
    print "{0}:{1}".format(patient_item,ds.data_element(patient_item).value)

# StudyInstanceUID
# SeriesInstanceUID
# Modality
# BodyPartExamined
# AccessionNumber
# PatientPosition
# PixelData
# PixelSpacing
# SliceThickness
# SpacingBetweenSlices
# WindowCenter
# WindowWidth
# ImagePositionPatient
# ImageOrientationPatient
# RescaleSlope
# RescaleIntercept


# print "StudyInstanceUID {0}".format(ds.StudyInstanceUID)
# print "SeriesInstanceUID {0}".format(ds.SeriesInstanceUID)
# print "Modality {0}".format(ds.Modality)
# print "BodyPartExamined {0}".format(ds.BodyPartExamined)
# print "AccessionNumber {0}".format(ds.AccessionNumber)
# print "PatientPosition {0}".format(ds.PatientPosition)
# print "PixelData {0}".format(ds.PixelData)
# print "PixelSpacing {0}".format(ds.PixelSpacing)
# print "SliceThickness {0}".format(ds.SliceThickness)

