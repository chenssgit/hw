package css.test.jdk8;

import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class NewFeature {

	public void testLambda(){
		List<String> list=Arrays.asList("z","bb","cd");
		Collections.sort(list, (s1,s2)->s1.compareTo(s2));
		System.out.println(list);
	}
	public static void main(String[] args) {
		NewFeature t=new NewFeature();
		t.testLambda();
	}

}
