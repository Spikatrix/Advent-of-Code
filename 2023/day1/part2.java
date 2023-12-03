import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;

public class part2 {
	private static String[] numStrs = { "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" };

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

			char firstChar = '0';

			int firstNumber = -1;
			int firstNumberIndex = -1;
			for (int j = 0; j < line.length(); j++) {
				char c = line.charAt(j);
				if (Character.isDigit(c)) {
					firstNumber = Character.getNumericValue(c);
					firstNumberIndex = j;
					break;
				}
			}

			int firstWordNumber = -1;
			int firstWorkNumberIndex = -1;
			for (int k = 0; k < numStrs.length; k++) {
				int numStrIndex = line.indexOf(numStrs[k]);
				if (numStrIndex != -1 && (firstWorkNumberIndex == -1 || numStrIndex < firstWorkNumberIndex)) {
					firstWorkNumberIndex = numStrIndex;
					firstWordNumber = k + 1;
				}
			}

			if (firstNumber == -1) {
				firstChar = Character.forDigit(firstWordNumber, 10);
			} else if (firstWordNumber == -1) {
				firstChar = Character.forDigit(firstNumber, 10);
			} else if (firstNumberIndex < firstWorkNumberIndex) {
				firstChar = Character.forDigit(firstNumber, 10);
			} else {
				firstChar = Character.forDigit(firstWordNumber, 10);
			}

			char lastChar = '0';

			int lastNumber = -1;
			int lastNumberIndex = -1;
			for (int j = line.length() - 1; j >= 0; j--) {
				char c = line.charAt(j);
				if (Character.isDigit(c)) {
					lastNumber = Character.getNumericValue(c);
					lastNumberIndex = j;
					break;
				}
			}

			int lastWordNumber = -1;
			int lastWorkNumberIndex = -1;
			for (int k = 0; k < numStrs.length; k++) {
				int numStrIndex = line.lastIndexOf(numStrs[k]);
				if (numStrIndex != -1 && (lastWorkNumberIndex == -1 || numStrIndex > lastWorkNumberIndex)) {
					lastWorkNumberIndex = numStrIndex;
					lastWordNumber = k + 1;
				}
			}

			if (lastNumber == -1) {
				lastChar = Character.forDigit(lastWordNumber, 10);
			} else if (lastWordNumber == -1) {
				lastChar = Character.forDigit(lastNumber, 10);
			} else if (lastNumberIndex > lastWorkNumberIndex) {
				lastChar = Character.forDigit(lastNumber, 10);
			} else {
				lastChar = Character.forDigit(lastWordNumber, 10);
			}

			total += Integer.parseInt(new StringBuilder().append(firstChar).append(lastChar).toString());
		}

		System.out.println(total);
	}
}