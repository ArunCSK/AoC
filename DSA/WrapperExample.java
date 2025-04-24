import java.util.ArrayList;

public class WrapperExample {
    public static void main(String[] args) {
        int num = 10;
        Integer numObj = Integer.valueOf(num); // Boxing: primitive to object
        int numPrimitive = numObj.intValue(); // Unboxing: object to primitive

        System.out.println("Primitive: " + num);
        System.out.println("Wrapper Object: " + numObj);
        System.out.println("Converted Back to Primitive: " + numPrimitive);
    }
}

// public class Main {
//     public static void main(String[] args) {
//         System.out.println("Hello, World!");
//     }
// }