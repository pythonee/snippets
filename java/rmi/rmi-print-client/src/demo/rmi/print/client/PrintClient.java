package demo.rmi.print.client;

import java.rmi.Naming;

import demo.rmi.print.common.RemotePrinter;

public class PrintClient {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		try {
			System.setSecurityManager(new SecurityManager());
		
			RemotePrinter printer = (RemotePrinter) Naming.lookup("rmi://localhost:1099/printer");
			
			int jobID = printer.submitJob("Hello world");
			
			System.out.println(jobID+" "+printer.getPrinterStatus());
			
		} catch (Exception e) {
			e.printStackTrace();
		}

	}

}
