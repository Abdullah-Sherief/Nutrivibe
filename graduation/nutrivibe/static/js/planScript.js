 
 
 function countCalories() {
    // Get input values
    var age = parseInt(document.getElementById("age").value);
    var weight = parseFloat(document.getElementById("weight").value);
    var height = parseFloat(document.getElementById("height").value);
    var activity = parseInt(document.getElementById("activity").value);
    var gender = document.querySelector('input[name="radio"]:checked').id;
   

    
    // Calculate BMR (Basal Metabolic Rate) based on gender
    var bmr;
    if (gender === "m") {
      bmr = 10 * weight + 6.25 * height - 5 * age + 5;
    } else {
      bmr = 10 * weight + 6.25 * height - 5 * age - 161;
    }

    // Adjust BMR based on activity level
    var calories;
    switch (activity) {
      case 1:
        calories = bmr * 1.2;
        break;
      case 2:
        calories = bmr * 1.375;
        break;
      case 3:
        calories = bmr * 1.55;
        break;
      case 4:
        calories = bmr * 1.725;
        break;
      case 5:
        calories = bmr * 1.9;
        break;
      default:
        calories = bmr * 1.2; // Default to sedentary activity level
    }

    // Display result
    document.getElementById("result").textContent = calories.toFixed(2);
  }

  

  
