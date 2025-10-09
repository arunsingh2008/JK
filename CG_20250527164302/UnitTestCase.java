// Disclaimer: This output contains AI-generated content; user is advised to review it before consumption.
//*Start of AI Generated Content*

java
java
/**
 * Unit Test Cases for UserRegistrationAPI
 *
 * @author [Your Name]
 * @version 1.0
 * @since 2023-02-20
 */
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.MockitoAnnotations;
import org.springframework.http.ResponseEntity;

import com.mongodb.client.MongoCollection;
import com.mongodb.client.model.Filters;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.Mockito.doReturn;
import static org.mockito.Mockito.verify;

public class UserRegistrationAPITest {

    @Mock
    private MongoCollection<org.bson.Document> collection;

    @InjectMocks
    private UserRegistrationAPI userRegistrationAPI;

    private UserRegistrationRequest userRegistrationRequest;
    private ForgotPasswordRequest forgotPasswordRequest;
    private PersonalInfoRequest personalInfoRequest;
    private LoginRequest loginRequest;
    private LogoutRequest logoutRequest;

    @BeforeEach
    public void setup() {
        MockitoAnnotations.initMocks(this);
        userRegistrationRequest = new UserRegistrationRequest();
        forgotPasswordRequest = new ForgotPasswordRequest();
        personalInfoRequest = new PersonalInfoRequest();
        loginRequest = new LoginRequest();
        logoutRequest = new LogoutRequest();
    }

    /**
     * Test Case: Successful User Registration
     *
     * @throws Exception
     */
    @Test
    public void testRegisterUser_Success() throws Exception {
        // Arrange
        userRegistrationRequest.setEmailOrPhone("test@example.com");
        userRegistrationRequest.setPassword("P@ssw0rd");
        userRegistrationRequest.setConfirmPassword("P@ssw0rd");
        userRegistrationRequest.setSecurityQuestion("securityQuestion");

        doReturn(org.bson.Document.parse("{}")).when(collection).insertOne(any());

        // Act
        ResponseEntity<String> response = userRegistrationAPI.registerUser(userRegistrationRequest);

        // Assert
        assertEquals(HttpStatus.CREATED, response.getStatusCode());
        assertEquals("User registered successfully", response.getBody());
    }

    /**
     * Test Case: Failed User Registration - Invalid Email/Phone
     *
     * @throws Exception
     */
    @Test
    public void testRegisterUser_InvalidEmailOrPhone() throws Exception {
        // Arrange
        userRegistrationRequest.setEmailOrPhone("invalid");

        // Act and Assert
        Exception exception = assertThrows(Exception.class, () -> userRegistrationAPI.registerUser(userRegistrationRequest));
        assertEquals("Invalid email address or phone number", exception.getMessage());
    }

    /**
     * Test Case: Successful Forgot Password
     *
     * @throws Exception
     */
    @Test
    public void testForgotPassword_Success() throws Exception {
        // Arrange
        forgotPasswordRequest.setSecurityQuestion("securityQuestion");

        doReturn(org.bson.Document.parse("{}")).when(collection).find(any());

        // Act
        ResponseEntity<String> response = userRegistrationAPI.forgotPassword(forgotPasswordRequest);

        // Assert
        assertEquals(HttpStatus.OK, response.getStatusCode());
        assertEquals("Password reset link sent successfully", response.getBody());
    }

    /**
     * Test Case: Failed Forgot Password - Incorrect Security Question
     *
     * @throws Exception
     */
    @Test
    public void testForgotPassword_IncorrectSecurityQuestion() throws Exception {
        // Arrange
        forgotPasswordRequest.setSecurityQuestion("incorrect");

        doReturn(null).when(collection).find(any());

        // Act and Assert
        Exception exception = assertThrows(Exception.class, () -> userRegistrationAPI.forgotPassword(forgotPasswordRequest));
        assertEquals("Incorrect security question answer", exception.getMessage());
    }

    /**
     * Test Case: Successful Save Personal Info
     *
     * @throws Exception
     */
    @Test
    public void testSavePersonalInfo_Success() throws Exception {
        // Arrange
        personalInfoRequest.setEmailOrPhone("test@example.com");
        personalInfoRequest.setName("John Doe");
        personalInfoRequest.setAge("25");
        personalInfoRequest.setSex("Male");
        personalInfoRequest.setAddress("123 Main St");

        doReturn(org.bson.Document.parse("{}")).when(collection).find(any());
        doReturn(org.bson.Document.parse("{}")).when(collection).updateOne(any(), any());

        // Act
        ResponseEntity<String> response = userRegistrationAPI.savePersonalInfo(personalInfoRequest);

        // Assert
        assertEquals(HttpStatus.OK, response.getStatusCode());
        assertEquals("Personal information saved successfully", response.getBody());
    }

    /**
     * Test Case: Failed Save Personal Info - Invalid Name
     *
     * @throws Exception
     */
    @Test
    public void testSavePersonalInfo_InvalidName() throws Exception {
        // Arrange
        personalInfoRequest.setName("invalid");

        // Act and Assert
        Exception exception = assertThrows(Exception.class, () -> userRegistrationAPI.savePersonalInfo(personalInfoRequest));
        assertEquals("Invalid name", exception.getMessage());
    }

    /**
     * Test Case: Successful Login
     *
     * @throws Exception
     */
    @Test
    public void testLogin_Success() throws Exception {
        // Arrange
        loginRequest.setEmailOrPhone("test@example.com");
        loginRequest.setPassword("P@ssw0rd");

        doReturn(org.bson.Document.parse("{\"password\": \"P@ssw0rd\"}")).when(collection).find(any());

        // Act
        ResponseEntity<String> response = userRegistrationAPI.login(loginRequest);

        // Assert
        assertEquals(HttpStatus.OK, response.getStatusCode());
        assertEquals("Login successful", response.getBody());
    }

    /**
     * Test Case: Failed Login - Incorrect Email/Password
     *
     * @throws Exception
     */
    @Test
    public void testLogin_IncorrectEmailOrPassword() throws Exception {
        // Arrange
        loginRequest.setEmailOrPhone("test@example.com");
        loginRequest.setPassword("incorrect");

        doReturn(org.bson.Document.parse("{\"password\": \"P@ssw0rd\"}")).when(collection).find(any());

        // Act and Assert
        Exception exception = assertThrows(Exception.class, () -> userRegistrationAPI.login(loginRequest));
        assertEquals("Incorrect email or password", exception.getMessage());
    }

    /**
     * Test Case: Successful Logout
     *
     * @throws Exception
     */
    @Test
    public void testLogout_Success() throws Exception {
        // Act
        ResponseEntity<String> response = userRegistrationAPI.logout(logoutRequest);

        // Assert
        assertEquals(HttpStatus.OK, response.getStatusCode());
        assertEquals("Logout successful", response.getBody());
    }
}


//*End of AI Generated Content*