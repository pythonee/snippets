package string;
import junit.framework.TestCase;


public class ReverseTest extends TestCase {

    Reverse re = new Reverse();
    protected void setUp() throws Exception {
    }

    public void testReverse(){
       String str = "hello world";
       assertEquals("dlrow olleh", re.reverse(str));
    }
}
