class FootballDataManagement:
    def __init__(self, AddNewField, Displayfieldlist, EditFieldInformation, DeleteField):
        self.add_new_field = AddNewField
        self.display_field_list = Displayfieldlist
        self.edit_field_information = EditFieldInformation
        self.delete_field = DeleteField
    def manage_fields(self):
        return (f"Add New Field:{self.add_new_field}, Display Field List:{self.display_field_list}, Edit Field Information:{self.edit_field_information}, Delete Field:{self.delete_field}")    
times = int(input("How many times do you want to add the football fields? "))
for i in range (times): 
    Choice = input("Do you want to create a new field? (yes/no): ")
    if Choice.lower()=="yes":
        field_name = input("Enter the name of the new field: ")
        field_location = input("Enter the location of the new field: ")
        field_capacity = input("Enter the capacity of the new field: ")
        football_data_management = FootballDataManagement(field_name, field_location, field_capacity, "None")
        print(football_data_management.manage_fields())
        with open(" Output.txt", "a+", encoding="utf-8") as f:
            f.write(football_data_management.manage_fields() + "\n")
    else:
        print("No new field added.")
