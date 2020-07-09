import java.lang.reflect.Array;
import java.util.*;

public class App {
    public static void main(final String[] args)  {
        fibonacci f = new fibonacci();
        List result = f.calcularFibonacci(14);
        System.out.println(result);
        System.out.println(f.isFibonnaci(1));
    }
}