import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

public class T11 {

	static class Option {
		final int[] option;

		Option(int[] option) {
			this.option = option;
		}

		@Override
		public int hashCode() {
			final int prime = 31;
			int result = 1;

			for (int i = 0; i < option.length; i++) {
				result = prime * result + option[i];
			}

			return result;
		}

		@Override
		public boolean equals(Object obj) {
			Option w = (Option)obj;
			for (int i = 0; i < option.length; i++) {
				if (option[i] != w.option[i]) {
					return false;
				}
			}

			return true;
		}
	}

	// TODO: generate INPUT
	static int[] INPUT = new int[] {
		Integer.parseInt("100000000111111", 2),
		Integer.parseInt("010101010000000", 2),
		Integer.parseInt("001010101000000", 2),
		Integer.parseInt("000000000000000", 2)
	};

	static Set<Option> cache = new HashSet<>(1000000);

	static final int floor_mask = 1 << (getInputSize() * 2);
	static final int goal = floor_mask - 1;
	static final Set<Integer> allCombinations = new HashSet<>();
	static int g_mask = 0;
	static int m_mask = 0;

	static int it = 0;

	static int getFloor(int[] option) {
		for (int i = 0; i < option.length; i++) {
			if ((option[i] & floor_mask) > 0) {
				return i;
			}
		}

		throw new IllegalArgumentException();
	}

	static boolean notLogicalImplication(int p, int q) {
		return (p & ~q) == 0;
	}

	static boolean isValidOptionRow(int row) {
		int generators = row & g_mask;
		if (generators == 0) {
			return true;
		}

		int chips = row & m_mask;
		return notLogicalImplication((chips << 1), generators);
	}

	static int[] generateUp(int floor, int[] option, int movedItems) {
		if (floor == 3) {
			return null;
		}

		int cf = option[floor] - movedItems - floor_mask;
		if (!isValidOptionRow(cf)) {
			return null;
		}

		int uf = option[floor + 1] + movedItems;
		if (!isValidOptionRow(uf)) {
			return null;
		}

		if (floor == 2 && uf == goal) {
			System.out.println("FOUND IT: " + it);
			System.exit(0);
		}

		if (floor == 0) {
			return new int[] {
				cf,
				uf + floor_mask,
				option[2],
				option[3]
			};
		}

		if (floor == 1) {
			return new int[] {
				option[0],
				cf,
				uf + floor_mask,
				option[3]
			};
		}

		if (floor == 2) {
			return new int[] {
				option[0],
				option[1],
				cf,
				uf + floor_mask,
			};
		}

		throw new IllegalArgumentException();
	}

	static int[] generateDown(int floor, int[] option, int movedItems) {
		if (floor == 0) {
			return null;
		}

		int cf = option[floor] - movedItems - floor_mask;
		if (!isValidOptionRow(cf)) {
			return null;
		}

		int df = option[floor - 1] + movedItems;
		if (!isValidOptionRow(df)) {
			return null;
		}

		if (floor == 1) {
			return new int[] {
				df + floor_mask,
				cf,
				option[2],
				option[3]
			};
		}

		if (floor == 2) {
			return new int[] {
				option[0],
				df + floor_mask,
				cf,
				option[3]
			};
		}

		if (floor == 3) {
			return new int[] {
				option[0],
				option[1],
				df + floor_mask,
				cf
			};
		}

		throw new IllegalArgumentException();
	}

	static boolean cacheStuff(int[] option) {
		if (option == null) {
			return false;
		}

		return cache.add(new Option(option));
	}

	static Set<int[]> getPossibleOptions(int[] option) {
		int floor = getFloor(option);
		int row = option[floor];

		Set<int[]> result = new HashSet<>(allCombinations.size() * 2);
		for (Integer x : allCombinations) {
			if (notLogicalImplication(x, row)) {
				int[] up = generateUp(floor, option, x);
				if (cacheStuff(up)) {
					result.add(up);
				}

				int[] down = generateDown(floor, option, x);
				if (cacheStuff(down)) {
					result.add(down);
				}
			}
		}

		return result;
	}

	public static void main(String[] args) {
		int inputSize = getInputSize();

		for (int i = 0; i < inputSize*2; i++) {
			allCombinations.add(1 << i);
			for (int j = 0; j < i; j++) {
				allCombinations.add((1 << i) + (1 << j));
			}
		}

		for (int i = 0; i < inputSize*2; i++) {
			if (i % 2 == 0) {
				m_mask += 1 << i;
			} else {
				g_mask += 1 << i;
			}
		}

		Set<int[]> options = new HashSet<>();
		options.add(INPUT);

		long start = System.nanoTime();
		while(true) {
			it++;

			options = options.parallelStream()
				.map(T11::getPossibleOptions)
				.flatMap(Set::stream)
				.collect(Collectors.toSet());

			System.out.println(it + "    " + options.size() + "   " + "Time taken(s): " + (System.nanoTime() - start) / 1.0e9);
		}
	}

	static int getInputSize() {
		return Integer.toBinaryString(INPUT[0]).length() / 2;
	}
}
