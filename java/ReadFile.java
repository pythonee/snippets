try {
  		File file = new File("C:\\Users\\WangFei\\Desktop\\DML.txt");
			
			FileInputStream fstream = new FileInputStream(file);
			DataInputStream in = new DataInputStream(fstream);
			BufferedReader br = new BufferedReader(new InputStreamReader(in));

			Scanner scanner = new Scanner(br).useDelimiter(Pattern.compile(
					"^\\s*$", Pattern.MULTILINE));
			
			while(scanner.hasNext()) {
				String paragraph = scanner.next();
				String[] lines = paragraph.split("\\n");
				StringBuilder sb = new StringBuilder();

				for (String line : lines) {
					if (line.length() > 0 && !line.startsWith("#")) {
						sb.append(line);
					}
				}	    		
			}
} catch (IOException x) {
  System.err.println(x);
}
