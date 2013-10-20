    package edu.usf.csee.media.jai;  
      
    import java.awt.*;  
    import java.awt.image.*;  
    import java.awt.image.renderable.ParameterBlock;  
    import java.util.*;  
    import javax.media.jai.*;  
      
    /** Calculates Grey Level Cooccurence Matrix statistics from an image. 
     * 
     * @author Mark Powell 
     * @author Mark.Powell@computer.org 
     * @version beta  
     
     Copyright (C) 2000  Mark Powell 
      
     This program is free software; you can redistribute it and/or 
     modify it under the terms of the GNU General Public License 
     as published by the Free Software Foundation. 
      
     This program is distributed in the hope that it will be useful, 
     but WITHOUT ANY WARRANTY; without even the implied warranty of 
     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the 
     GNU General Public License for more details. 
      
     You should have received a copy of the GNU General Public License 
     along with this program; if not, write to the Free Software 
     Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA. 
     
     */  
    public class GLCMTextureOpImage extends UntiledOpImage {  
      
      /** Constructs GLCMTextureOpImage.  Image dimensions are copied from the 
       * source image.  The tile grid layout, SampleModel, and ColorModel may 
       * optionally be specified by an ImageLayout object  
       * To specify the distance and direction of two pixels to compare, supply 
       * the horizontal distance and vertical distance between two pixels to  
       * compare.  For example, distance 1, direction 45 degrees would be  
       * xoffset = +1, yoffset = -1, and direction 315 degrees would be  
       * xoffset = +1, yoffset = +1. 
       * @param source a RenderedImage 
       * @param layout an ImageLayout optionally containing the tile grid layout, 
       * @param xoffset the horizontal distance between two pixels compared for the GLCM. 
       * @param yoffset the vertical distance between two pixels compared for the GLCM. 
       * SampleModel, and ColorModel or null. 
       */  
      public GLCMTextureOpImage(RenderedImage source,  
                    ImageLayout layout,  
                    Integer xoffset,  
                    Integer yoffset) {  
        super(source, null, layout);  
        this.xoffset = xoffset.intValue();  
        this.yoffset = yoffset.intValue();  
      }  
      
      /** calculates GLCM texture statistics. 
       * @param src the source raster. 
       * @param dst the resultant connected component image. 
       * @param destRect the rectangle within the OpImage to be computed */  
      protected void computeImage(Raster src[],  
                      WritableRaster dst,  
                      Rectangle destRect) {  
        Raster2 source = new Raster2(src[0]);  
        WritableRaster2 dest = new WritableRaster2(dst);  
        int width = source.getWidth(), height = source.getHeight();  
        double glcm[][] = new double[256][256];  
          
        /* Implement op here */  
        //tally up the pixel spatial relations into a GLCM  
        for (int u = 0; u < width; u++)  
        {  
          for (int v = 0; v < height; v++)  
          {  
        int u2 = u + xoffset, v2 = v + yoffset;  
        if (u2 >= 0 && u2 < width &&  
            v2 >= 0 && v2 < height)  
        {  
          glcm[source.grey(u, v)][source.grey(u2, v2)]++;  
        }  
          }  
        }  
        for (int u = 0; u < 256; u++)  
        {  
          for (int v = 0; v < 256; v++)  
          {  
        glcm[u][v] /= (double)(width*height);  
          }  
        }  
      
        //compute useful features  
        double mtRowMean=0., mtColumnMean=0.;  
        double mtRowSigmaSquared=0., mtColumnSigmaSquared=0., tempSum=0.;  
        double rowSum[] = new double[256], columnSum[] = new double[256];  
        double rowMean=0., columnMean=0., rowColumnMean=0., tempProduct=0.;  
        double rowSigmaSquared=0., columnSigmaSquared=0.;  
      
        energy=0;  
        entropy=0;  
        mtCorrelation=0;  
        haralickCorrelation1=0;  
        haralickCorrelation2=0;  
        inverseDifferenceMoment=0;  
        inertia=0;  
        mtShade=0;  
        mtProminence=0;  
        int i, j;  
        for (i = 0; i < 256; i++)  
        {  
          for (j = 0; j < 256; j++)  
          {  
        // Energy: if there are a whole lot of ones everywhere (not much repetition) then   
        // the value is small, but if there is repetition, the GLCM entries will be large,  
        // and the squares of them will be even larger.  
            energy += glcm[i][j] * glcm[i][j];  
      
        // Entropy  
        if (glcm[i][j] > 0)  
          entropy -= (double)glcm[i][j] * Math.log((double)glcm[i][j]);  
      
        mtRowMean += (double)glcm[i][j] * (double)i;  
        mtColumnMean += (double)glcm[i][j] * (double)j;  
        rowSum[i] += (double)glcm[i][j];  
        columnSum[j] += (double)glcm[i][j];  
      
        // Inverse Difference Moment: measure of local homogeneity  
        inverseDifferenceMoment += 1.0/(1.0 + (i-j)*(i-j)) * (double)glcm[i][j];  
      
        // Inertia  
        inertia += (double)(i-j)*(i-j) * (double)glcm[i][j];  
      
          }  
        }  
      
        for (i = 0; i < 256; i++)  
        {  
          rowMean += rowSum[i];  
          columnMean += columnSum[i];  
          mtRowSigmaSquared += ((double)i-mtRowMean)*((double)i-mtRowMean)*rowSum[i];  
          mtColumnSigmaSquared += ((double)i-mtColumnMean)*((double)i-mtColumnMean)*columnSum[i];  
        }  
        rowMean /= 256.;  
        columnMean /= 256.;  
        rowColumnMean = rowMean * columnMean;  
      
        for (i = 0; i < 256; i++)  
        {  
          rowSigmaSquared += (rowSum[i] - rowMean)*(rowSum[i] - rowMean);  
          columnSigmaSquared += (columnSum[i] - columnMean)*(columnSum[i] - columnMean);  
        }  
        rowSigmaSquared /= (256. - 1.);  
        columnSigmaSquared /= (256. - 1.);  
      
        for (i = 0; i < 256; i++)  
        {  
          for (j = 0; j < 256; j++)  
          {  
        mtCorrelation += ((double)i-mtRowMean)*((double)j-mtColumnMean) * (double)glcm[i][j];  
        tempSum = (double) (i + j) - mtRowMean - mtColumnMean;  
        tempProduct = tempSum * tempSum * tempSum * (double)glcm[i][j];  
        mtShade += tempProduct;  
        mtProminence += tempProduct * tempSum;  
      
        /* Correlation a la Haralick: interpretation 1 */  
        haralickCorrelation1 += (double)(i*j) * (double)glcm[i][j] - rowColumnMean;    
      
        /* Correlation a la Haralick: interpretation 2 */     
        haralickCorrelation2 += (double)(i*j) * (double)glcm[i][j];   
          }  
        }  
        mtCorrelation /= Math.sqrt(mtRowSigmaSquared * mtColumnSigmaSquared);  
        haralickCorrelation1 /= Math.sqrt(rowSigmaSquared * columnSigmaSquared);  
        haralickCorrelation2 -= rowColumnMean;  
        haralickCorrelation2 /= Math.sqrt(rowSigmaSquared * columnSigmaSquared);   
      
        System.out.print(energy);  
        System.out.print(" "+ entropy);  
        System.out.print(" "+ mtCorrelation);  
        System.out.print(" "+ haralickCorrelation1);  
        System.out.print(" "+ haralickCorrelation2);  
        System.out.print(" "+ inverseDifferenceMoment);  
        System.out.print(" "+ inertia);  
        System.out.print(" "+ mtShade);  
        System.out.println(" "+ mtProminence);  
      }  
      
      /* 
        PRIVATE METHODS 
      */  
      
      private int xoffset = 1;  
      private int yoffset = 1;  
      private double energy=0, entropy=0, mtCorrelation=0, haralickCorrelation1=0, haralickCorrelation2=0, inverseDifferenceMoment=0, inertia=0, mtShade=0, mtProminence=0;  
    }  
