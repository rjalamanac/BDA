import java.io.IOException;
import java.util.*;

import javax.naming.Context;

import org.apache.hadoop.mapreduce.*;
import org.apache.hadoop.mapreduce.lib.input.*;
import org.apache.hadoop.mapreduce.lib.output.*;
import org.apache.hadoop.conf.*;
import org.apache.hadoop.io.*;
import org.apache.hadoop.util.*;
import org.w3c.dom.Text;
import org.apache.hadoop.fs.*;

public class ShowDepartementsWithMoreOf200Import {

	public static class Map extends Mapper<LongWritable, Text, Text, IntWritable> {
		private Text word = new Text("1");
		private IntWritable importeData = new IntWritable(1);

		@Override
		public void map(LongWritable key, Text value, Context context)
				throws IOException, InterruptedException {
			String line = value.toString();
			String[] splitedArrayLineFile = line.split(",");
			try {
				int valor = Integer.parseInt(splitedArrayLineFile[4].split(".")[0]);
				if (splitedArrayLineFile.length == 5 && valor > 200) {
					importeData.set(valor);
					word.set(splitedArrayLineFile[0]);
					context.write(word, importeData);
				}

			} catch (NumberFormatException ex) {

			} catch (ArrayIndexOutOfBoundsException ex) {

			}

		}
	}

	public static class Reduce extends Reducer<Text, IntWritable, Text, IntWritable> {
		@Override
		public void reduce(Text key, Iterable<IntWritable> values, Context context)
				throws IOException, InterruptedException {
			int sum = 0;
			for (IntWritable val : values) {
				sum += val.get();
			}
			context.write(key, new IntWritable(sum));
		}

	}

	public static void main(String[] args) throws Exception {
		Job job = Job.getInstance();
		job.setJarByClass(ShowDepartementsWithMoreOf200Import.class);
		job.setJobName("ShowDepartementsWithMoreOf200Import");

		job.setOutputKeyClass(Text.class);
		job.setOutputValueClass(IntWritable.class);

		job.setMapperClass(Map.class);
		job.setCombinerClass(Reduce.class);
		job.setReducerClass(Reduce.class);

		job.setInputFormatClass(TextInputFormat.class);
		job.setOutputFormatClass(TextOutputFormat.class);

		FileInputFormat.addInputPath(job, new Path(args[0]));
		FileOutputFormat.setOutputPath(job, new Path(args[1]));

		System.exit(job.waitForCompletion(true) ? 0 : 1);
	}
}