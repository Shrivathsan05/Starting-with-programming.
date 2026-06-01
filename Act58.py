#First, create a dictionary that consists of - id, name, class and subject integration of students. Then, write a program to retrieve unique entries and eliminate the rest.
StudentData = {
" ID1 " : {" Name " : " Sara", " Class " : " V", " SubjectIntegration " : " English, Math, Science "},
" ID2 " : {" Name " : " David", " Class " : " V", " SubjectIntegration " : " English, Math, Science "},
" ID3 " : {" Name " : " Sara", " Class " : " V", " SubjectIntegration " : " English, Math, Science "},
" ID4 " : {" Name " : " Surya", " Class " : " V", " SubjectIntegration " : " English, Math, Science "},
}
Result = {}
SeenKeys = []
for StudentID, Details in StudentData.items() :
    UniqueKey = (Details[" Name "], Details[" Class "], Details[" SubjectIntegration "])
    if UniqueKey not in SeenKeys :
        SeenKeys.append(UniqueKey)
        Result[StudentID] = Details
for s, k  in Result.items() :
    print(s, ":", k)