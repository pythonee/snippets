import java.util.LinkedList;

public class Producter extends Thread {
	public LinkedList<Integer> list;
	public final static int CAPACITY = 9;

	public Producter(LinkedList<Integer> list) {
		this.list = list;
	}

	@Override
	public void run() {
		while (true) {
			synchronized (list) {
				System.out.println(this.getClass().toString() + " "
						+ this.getId() + " thread, list size " + list.size());

				while (list.size() == CAPACITY) {
					try {
						list.wait();
					} catch (InterruptedException e) {
						e.printStackTrace();
					}
				}

				if (list.size() < CAPACITY) {
					try {
						sleep(1000);
						list.add(0);
						list.notifyAll();
					} catch (InterruptedException e) {
						e.printStackTrace();
					}
				}
			}
		}
	}
}
