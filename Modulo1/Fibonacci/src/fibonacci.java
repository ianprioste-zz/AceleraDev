import java.util.ArrayList;
import java.util.List;

public class fibonacci{
    List listfibonacci = new ArrayList();

    public List calcularFibonacci(int num) {

            for (int i=0; i<num; i++){
                if(i<2){
                    listfibonacci.add(1);
                } else{
                    int temp = (int) listfibonacci.get(i-2)+ (int) listfibonacci.get(i-1);
                    listfibonacci.add(temp);     
                }
            }
        return listfibonacci;
    }

    public boolean isFibonnaci(int num){
        return listfibonacci.contains(num);
    }
}