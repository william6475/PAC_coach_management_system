
console.log("hello");
console.log("hellos");
function Restrict_enrolment_form_options() {
  //If PAC is selected in the account type dropdown
  if (document.getElementById("Account_type_dropdown").value === "PAC") {
    //Show the PAC fields
    document.getElementById("PAC_first_name_label").style.display = "block";
    document.getElementById("PAC_first_name").style.display = "block";
    document.getElementById("PAC_last_name_label").style.display = "block";
    document.getElementById("PAC_last_name").style.display = "block";
    document.getElementById("PAC_email_label").style.display = "block";
    document.getElementById("PAC_email").style.display = "block";
    document.getElementById("PAC_department_label").style.display = "block";
    document.getElementById("PAC_department").style.display = "block";
    //Enable the PAC fields
    document.getElementById("PAC_first_name").disabled = false;
    document.getElementById("PAC_last_name").disabled = false;
    document.getElementById("PAC_email").disabled = false;
    document.getElementById("PAC_department").disabled = false;
    //Hide the student form elements
    document.getElementById("Student_number").style.display = "none";
    document.getElementById("Student_number_label").style.display = "none";
    document.getElementById("Student_first_name_label").style.display = "none";
    document.getElementById("Student_first_name").style.display = "none";
    document.getElementById("Student_last_name_label").style.display = "none";
    document.getElementById("Student_last_name").style.display = "none";
    document.getElementById("Student_email_label").style.display = "none";
    document.getElementById("Student_email").style.display = "none";
    document.getElementById("Student_course_label").style.display = "none";
    document.getElementById("Student_course").style.display = "none";
    document.getElementById("Student_year_group_label").style.display = "none";
    document.getElementById("Student_year_group").style.display = "none";
    document.getElementById("Student_assigned_pac_label").style.display = "none";
    document.getElementById("Student_assigned_pac").style.display = "none";
    //Disable the student fields
    document.getElementById("Student_number").disabled = true;
    document.getElementById("Student_first_name").disabled = true;
    document.getElementById("Student_last_name").disabled = true;
    document.getElementById("Student_email").disabled = true;
    document.getElementById("Student_course").disabled = true;
    document.getElementById("Student_year_group").disabled = true;
    document.getElementById("Student_assigned_pac").disabled = true;
  }
  //If student is selected in the account type dropdown
  if (document.getElementById("Account_type_dropdown").value === "Student") {
    //Show the student fields
    document.getElementById("Student_number").style.display = "block";
    document.getElementById("Student_number_label").style.display = "block";
    document.getElementById("Student_first_name_label").style.display = "block";
    document.getElementById("Student_first_name").style.display = "block";
    document.getElementById("Student_last_name_label").style.display = "block";
    document.getElementById("Student_last_name").style.display = "block";
    document.getElementById("Student_email_label").style.display = "block";
    document.getElementById("Student_email").style.display = "block";
    document.getElementById("Student_course_label").style.display = "block";
    document.getElementById("Student_course").style.display = "block";
    document.getElementById("Student_year_group_label").style.display = "block";
    document.getElementById("Student_year_group").style.display = "block";
    document.getElementById("Student_assigned_pac_label").style.display = "block";
    document.getElementById("Student_assigned_pac").style.display = "block";
    //Enable the student fields
    document.getElementById("Student_number").disabled = false;
    document.getElementById("Student_first_name").disabled = false;
    document.getElementById("Student_last_name").disabled = false;
    document.getElementById("Student_email").disabled = false;
    document.getElementById("Student_course").disabled = false;
    document.getElementById("Student_year_group").disabled = false;
    document.getElementById("Student_assigned_pac").disabled = false;
    //Hide the PAC form elements
    document.getElementById("PAC_first_name_label").style.display = "none";
    document.getElementById("PAC_first_name").style.display = "none";
    document.getElementById("PAC_last_name_label").style.display = "none";
    document.getElementById("PAC_last_name").style.display = "none";
    document.getElementById("PAC_email_label").style.display = "none";
    document.getElementById("PAC_email").style.display = "none";
    document.getElementById("PAC_department_label").style.display = "none";
    document.getElementById("PAC_department").style.display = "none";
    //Disable the PAC fields
    document.getElementById("PAC_first_name").disabled = true;
    document.getElementById("PAC_last_name").disabled = true;
    document.getElementById("PAC_email").disabled = true;
    document.getElementById("PAC_department").disabled = true;
  }
}