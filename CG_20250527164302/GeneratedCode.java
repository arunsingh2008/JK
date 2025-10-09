// Disclaimer: This output contains AI-generated content; user is advised to review it before consumption.
//*Start of AI Generated Content*

java
// UserRegistrationAPI.java

import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import com.mongodb.client.MongoClients;
import com.mongodb.client.MongoClient;
import com.mongodb.client.MongoCollection;
import com.mongodb.client.MongoDatabase;
import com.mongodb.client.model.Filters;

import javax.validation.Valid;
import java.util.ArrayList;
import java.util.List;
import java.util.regex.Pattern;

// Constants and Static Strings
public class Constants {
    public static final String EMAIL_REGEX = "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$";
    public static final String PHONE_NUMBER_REGEX = "^\\d{3}-\\d{3}-\\d{4}$";
    public static final String PASSWORD_REGEX = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)(?=.*[@$!%*?&])[A-Za-z\\d@$!%*?&]{8,}$";
    public static final String NAME_REGEX = "^[a-zA-Z]{2,}$";
    public static final String AGE_RANGE = "^(1[8-9]|[2-9][0-9])$";
    public static final String SEX_OPTIONS = "^(Male|Female)$";
    public static final String ADDRESS_REGEX = "^[a-zA-Z0-9\\s]{5,}$";
    public static final String MONGO_URI = "mongodb://localhost:27017";
    public static final String DATABASE_NAME = "user_database";
    public static final String COLLECTION_NAME = "users";
    public static final String FOOD_PREFERENCES[] = {"Indian", "Chinese", "French", "Italian", "Mexican", "Japanese", "Thai", "American", "Greek", "Mediterranean"};
}

@RestController
public class UserRegistrationAPI {

    private MongoClient mongoClient;
    private MongoDatabase database;
    private MongoCollection<org.bson.Document> collection;

    public UserRegistrationAPI() {
        this.mongoClient = MongoClients.create(Constants.MONGO_URI);
        this.database = mongoClient.getDatabase(Constants.DATABASE_NAME);
        this.collection = database.getCollection(Constants.COLLECTION_NAME);
    }

    // Function Variables for Hardcoded Values
    private String getMongoURI() { return Constants.MONGO_URI; }
    private String getDatabaseName() { return Constants.DATABASE_NAME; }
    private String getCollectionName() { return Constants.COLLECTION_NAME; }
    private String[] getFoodPreferences() { return Constants.FOOD_PREFERENCES; }

    // User Registration
    @PostMapping("/register")
    public ResponseEntity<String> registerUser(@Valid @RequestBody UserRegistrationRequest request) {
        try {
            validateEmailOrPhone(request.getEmailOrPhone());
            validatePassword(request.getPassword(), request.getConfirmPassword());
            validateSecurityQuestion(request.getSecurityQuestion());

            org.bson.Document userDoc = new org.bson.Document("emailOrPhone", request.getEmailOrPhone())
                    .append("password", request.getPassword())
                    .append("securityQuestion", request.getSecurityQuestion());

            collection.insertOne(userDoc);
            return new ResponseEntity<>("User registered successfully", HttpStatus.CREATED);
        } catch (Exception e) {
            return new ResponseEntity<>(e.getMessage(), HttpStatus.BAD_REQUEST);
        }
    }

    // Validate Email or Phone
    private void validateEmailOrPhone(String emailOrPhone) throws Exception {
        if (Pattern.matches(Constants.EMAIL_REGEX, emailOrPhone)) {
            // Email validation successful
        } else if (Pattern.matches(Constants.PHONE_NUMBER_REGEX, emailOrPhone)) {
            // Phone number validation successful
        } else {
            throw new Exception("Invalid email address or phone number");
        }
    }

    // Validate Password
    private void validatePassword(String password, String confirmPassword) throws Exception {
        if (!Pattern.matches(Constants.PASSWORD_REGEX, password)) {
            throw new Exception("Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, one number, and one special character");
        }
        if (!password.equals(confirmPassword)) {
            throw new Exception("Passwords do not match");
        }
    }

    // Validate Security Question
    private void validateSecurityQuestion(String securityQuestion) throws Exception {
        if (securityQuestion.isEmpty()) {
            throw new Exception("Security question cannot be empty");
        }
    }

    // Forgot Password
    @PostMapping("/forgot-password")
    public ResponseEntity<String> forgotPassword(@Valid @RequestBody ForgotPasswordRequest request) {
        try {
            org.bson.Document userDoc = collection.find(Filters.eq("securityQuestion", request.getSecurityQuestion())).first();
            if (userDoc != null) {
                // Send password reset link to user's email or phone
                return new ResponseEntity<>("Password reset link sent successfully", HttpStatus.OK);
            } else {
                throw new Exception("Incorrect security question answer");
            }
        } catch (Exception e) {
            return new ResponseEntity<>(e.getMessage(), HttpStatus.BAD_REQUEST);
        }
    }

    // Save User Personal Information
    @PostMapping("/save-personal-info")
    public ResponseEntity<String> savePersonalInfo(@Valid @RequestBody PersonalInfoRequest request) {
        try {
            validateName(request.getName());
            validateAge(request.getAge());
            validateSex(request.getSex());
            validateAddress(request.getAddress());

            org.bson.Document userDoc = collection.find(Filters.eq("emailOrPhone", request.getEmailOrPhone())).first();
            if (userDoc != null) {
                userDoc.append("name", request.getName())
                        .append("age", request.getAge())
                        .append("sex", request.getSex())
                        .append("address", request.getAddress())
                        .append("profilePicture", request.getProfilePicture());

                collection.updateOne(Filters.eq("emailOrPhone", request.getEmailOrPhone()), new org.bson.Document("$set", userDoc));
                return new ResponseEntity<>("Personal information saved successfully", HttpStatus.OK);
            } else {
                throw new Exception("User not found");
            }
        } catch (Exception e) {
            return new ResponseEntity<>(e.getMessage(), HttpStatus.BAD_REQUEST);
        }
    }

    // Validate Name
    private void validateName(String name) throws Exception {
        if (!Pattern.matches(Constants.NAME_REGEX, name)) {
            throw new Exception("Invalid name");
        }
    }

    // Validate Age
    private void validateAge(String age) throws Exception {
        if (!Pattern.matches(Constants.AGE_RANGE, age)) {
            throw new Exception("Age must be between 18 and 99");
        }
    }

    // Validate Sex
    private void validateSex(String sex) throws Exception {
        if (!Pattern.matches(Constants.SEX_OPTIONS, sex)) {
            throw new Exception("Invalid sex");
        }
    }

    // Validate Address
    private void validateAddress(String address) throws Exception {
        if (!Pattern.matches(Constants.ADDRESS_REGEX, address)) {
            throw new Exception("Invalid address");
        }
    }

    // Get Food Preferences
    @PostMapping("/get-food-preferences")
    public ResponseEntity<String[]> getFoodPreferences() {
        return new ResponseEntity<>(getFoodPreferences(), HttpStatus.OK);
    }

    // Login
    @PostMapping("/login")
    public ResponseEntity<String> login(@Valid @RequestBody LoginRequest request) {
        try {
            org.bson.Document userDoc = collection.find(Filters.eq("emailOrPhone", request.getEmailOrPhone())).first();
            if (userDoc != null && userDoc.getString("password").equals(request.getPassword())) {
                return new ResponseEntity<>("Login successful", HttpStatus.OK);
            } else {
                throw new Exception("Incorrect email or password");
            }
        } catch (Exception e) {
            return new ResponseEntity<>(e.getMessage(), HttpStatus.BAD_REQUEST);
        }
    }

    // Logout
    @PostMapping("/logout")
    public ResponseEntity<String> logout(@Valid @RequestBody LogoutRequest request) {
        // Logout implementation
        return new ResponseEntity<>("Logout successful", HttpStatus.OK);
    }
}

// Request Classes
class UserRegistrationRequest {
    private String emailOrPhone;
    private String password;
    private String confirmPassword;
    private String securityQuestion;

    // Getters and Setters
    public String getEmailOrPhone() { return emailOrPhone; }
    public void setEmailOrPhone(String emailOrPhone) { this.emailOrPhone = emailOrPhone; }
    public String getPassword() { return password; }
    public void setPassword(String password) { this.password = password; }
    public String getConfirmPassword() { return confirmPassword; }
    public void setConfirmPassword(String confirmPassword) { this.confirmPassword = confirmPassword; }
    public String getSecurityQuestion() { return securityQuestion; }
    public void setSecurityQuestion(String securityQuestion) { this.securityQuestion = securityQuestion; }
}

class ForgotPasswordRequest {
    private String securityQuestion;

    // Getters and Setters
    public String getSecurityQuestion() { return securityQuestion; }
    public void setSecurityQuestion(String securityQuestion) { this.securityQuestion = securityQuestion; }
}

class PersonalInfoRequest {
    private String emailOrPhone;
    private String name;
    private String age;
    private String sex;
    private String address;
    private String profilePicture;

    // Getters and Setters
    public String getEmailOrPhone() { return emailOrPhone; }
    public void setEmailOrPhone(String emailOrPhone) { this.emailOrPhone = emailOrPhone; }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public String getAge() { return age; }
    public void setAge(String age) { this.age = age; }
    public String getSex() { return sex; }
    public void setSex(String sex) { this.sex = sex; }
    public String getAddress() { return address; }
    public void setAddress(String address) { this.address = address; }
    public String getProfilePicture() { return profilePicture; }
    public void setProfilePicture(String profilePicture) { this.profilePicture = profilePicture; }
}

class LoginRequest {
    private String emailOrPhone;
    private String password;

    // Getters and Setters
    public String getEmailOrPhone() { return emailOrPhone; }
    public void setEmailOrPhone(String emailOrPhone) { this.emailOrPhone = emailOrPhone; }
    public String getPassword() { return password; }
    public void setPassword(String password) { this.password = password; }
}

class LogoutRequest {
    // Logout request implementation
}


//*End of AI Generated Content*