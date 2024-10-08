const submitBtn = document.querySelector('.submit-btn'); // Adjusted to use class selector
const warning = document.createElement('div'); // Create a warning div dynamically
warning.id = 'warning';
warning.style.display = 'none';
warning.style.color = 'red'; // Example styling
warning.textContent = 'Please fill in all required fields!';
document.querySelector('.container').appendChild(warning); // Append the warning to the container

const inputs = document.querySelectorAll('input[type="text"], input[type="radio"]');

submitBtn.addEventListener('click', (e) => {
  e.preventDefault();
  let allFilled = true;
  let filledFields = 0;

  inputs.forEach((input) => {
    if (input.type === 'text' && !input.value) {
      allFilled = false;
    }
    if (input.type === 'radio' && input.checked) {
      filledFields++;
    }
    if (input.type === 'text' && input.value) {
      filledFields++;
    }
  });

  if (!allFilled) {
    warning.style.display = 'block';
  } else {
    warning.style.display = 'none';
    // Code to process the form goes here
    alert("Form submitted successfully!"); // Example action
  }

  const progressBar = document.querySelector('.progress-bar'); // Ensure you have a progress bar element
  const totalFields = inputs.length;
  progressBar.style.width = `${(filledFields / totalFields) * 100}%`;
});

// Highlighting selected radio buttons
const radioGroups = ['marital-status', 'education', 'poutcome'];

radioGroups.forEach(group => {
  const radios = document.getElementsByName(group);
  radios.forEach(radio => {
    radio.addEventListener('change', () => {
      radios.forEach(r => {
        const label = r.closest('label'); // Use closest to get the label
        if (r.checked) {
          label.style.fontWeight = 'bold';
          label.style.opacity = '1';
        } else {
          label.style.opacity = '0.5';
          label.style.fontWeight = 'normal';
        }
      });
    });
  });
});
