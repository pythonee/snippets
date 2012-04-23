import java.util.LinkedList;

public class Consumer extends Thread {
	public LinkedList<Integer> list;

	public Consumer(LinkedList<Integer> list) {
		this.list = list;
	}

	@Override
	public void run() {
		while (true) {
			synchronized (list) {
				System.out.println(this.getClass().toString() + " "
						+ this.getId() + " thread, list size " + list.size());

				while (list.isEmpty()) {
					try {
						list.wait();
					} catch (InterruptedException e) {
						e.printStackTrace();
					}
				}

				if (list.size() > 0) {
					try {
						sleep(500);
						list.removeFirst();
						list.notifyAll();
					} catch (InterruptedException e) {
						e.printStackTrace();
					}
				}
			}
		}
	}
}
