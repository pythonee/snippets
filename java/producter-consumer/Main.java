import java.util.LinkedList;


public class Main {
	public static void main(String[] args){
		LinkedList<Integer> list = new LinkedList<Integer>();
		
		Producter prod1 = new Producter(list);
		Producter prod2 = new Producter(list);
		Producter prod3 = new Producter(list);
		prod1.start();
		prod2.start();
		prod3.start();

		Consumer cons1 = new Consumer(list);
		Consumer cons2 = new Consumer(list);
		cons1.start();
		cons2.start();
	}
}
