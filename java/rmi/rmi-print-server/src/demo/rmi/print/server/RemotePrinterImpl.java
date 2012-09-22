package demo.rmi.print.server;

import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.rmi.server.UnicastRemoteObject;

import demo.rmi.print.common.RemotePrinter;

@SuppressWarnings("serial")
public class RemotePrinterImpl extends UnicastRemoteObject implements RemotePrinter{

	protected RemotePrinterImpl() throws RemoteException {
		super();
		// TODO Auto-generated constructor stub
	}

	@Override
	public String getPrinterStatus() throws RemoteException {
		System.out.println("request printer status");
		return "OK";
	}

	@Override
	public boolean isComplete(int jobID) throws RemoteException {
		System.out.println("request job status");
		return true;
	}

	@Override
	public int submitJob(String text) throws RemoteException {
		System.out.println("submitted job " + text);
		return 0;
	}
	
	public static void main(String[] args) {
		try {
			Registry r = LocateRegistry.getRegistry();
			
			r.bind("printer", new RemotePrinterImpl());
			
			
			System.out.println("Server is ready");
			
			System.out.println(Registry.REGISTRY_PORT);
			
		} catch (Exception e) {
			// TODO: handle exception
			e.printStackTrace();
		}
	}

}
