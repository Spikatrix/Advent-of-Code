import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;

// I'm super rusty in Java so the code is probably terrible

public class part1 {
	public static void main(String[] args) {
		List<String> input;

		try {
			input = Files.readAllLines(Path.of("./input"));
		} catch (IOException e) {
			e.printStackTrace();
			return;
		}

		int lineCount = input.size();
		int total = 0;

		for (int i = 0; i < lineCount; i++) {
			String line = input.get(i);

			char firstNumber = '0';
			for (int j = 0; j < line.length(); j++) {
				char c = line.charAt(j);
				if (Character.isDigit(c)) {
					firstNumber = c;
					break;
				}
			}

			char lastNumber = '0';
			for (int j = line.length() - 1; j >= 0; j--) {
				char c = line.charAt(j);
				if (Character.isDigit(c)) {
					lastNumber = c;
					break;
				}
			}

			total += Integer.parseInt(new StringBuilder().append(firstNumber).append(lastNumber).toString());
		}

		System.out.println(total);
	}
}