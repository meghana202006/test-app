public class Calculator3 {

    public static void main(String[] args) {
        if (args.length < 3) {
            System.out.println("Usage: java Calculator2 <operation> <num1> <num2>");
            return;
        }

        int choice = Integer.parseInt(args[0]);  // Operation choice (1-5)
        double num1 = Double.parseDouble(args[1]);  // First number
        double num2 = Double.parseDouble(args[2]);  // Second number

        double result = 0;

        switch (choice) {
            case 1:
                result = num1 + num2;
                System.out.println("Result: " + result);
                break;
            case 2:
                result = num1 - num2;
                System.out.println("Result: " + result);
                break;
            case 3:
                result = num1 * num2;
                System.out.println("Result: " + result);
                break;
            case 4:
                if (num2 != 0) {
                    result = num1 / num2;
                    System.out.println("Result: " + result);
                } else {
                    System.out.println("Error! Division by zero.");
                }
                break;
            case 5:
                System.out.println("Exiting calculator...");
                break;
            default:
                System.out.println("Invalid choice! Please try again.");
        }
    }
}
